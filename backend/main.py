# backend/main.py
import io, time
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from PIL import Image

from .ai_model import predict_labels
from .waste_mapper import map_labels_to_category, CATEGORY_COLOR
from .database import append_log, read_logs, read_users
from .blockchain import get_chain
from .rewards import award_tokens
from .schemas import IoTData

app = FastAPI(title="Smart Waste System")

# Serve frontend
app.mount(
    "/static",
    StaticFiles(directory="frontend"),
    name="static"
)

chain = get_chain()

# ============================
# MAIN IMAGE CLASSIFICATION API
# ============================
@app.post("/upload-image")
async def upload_image(
    file: UploadFile = File(...),
    user_id: str = Form(...)
):
    try:
        contents = await file.read()
        pil_img = Image.open(io.BytesIO(contents)).convert("RGB")

        labels, decoded = predict_labels(pil_img, topk=7)
        category = map_labels_to_category(labels)

        if category == "cannot_be_classified":
            awarded = 0
            message = "Waste cannot be classified. Please segregate properly."
            status = "rejected"
        else:
            reward = award_tokens(user_id, "correct_segregation")
            awarded = reward.get("awarded", 0)
            message = f"{category.upper()} bin opened (simulated)."
            status = "accepted"

        record = {
            "timestamp": time.time(),
            "user_id": user_id,
            "item": file.filename,
            "predicted_category": category,
            "status": status
        }

        prev_hash = chain.latest()["hash"]
        block = chain.add_block(record)

        append_log({**record, "prev_hash": prev_hash, "hash": block["hash"]})

        return {
            "predicted_category": category,
            "top_labels": labels,
            "awarded_tokens": awarded,
            "message": message,
            "bin_color": CATEGORY_COLOR.get(category, {"name": "Rejected"})["name"]
        }

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

# ============================
# IoT Endpoint (unchanged)
# ============================
@app.post("/iot")
async def iot_post(data: IoTData):
    record = {
        "timestamp": data.timestamp or time.time(),
        "user_id": data.device_id,
        "item": data.action,
        "predicted_category": data.meta or {},
        "status": "iot_event"
    }

    prev_hash = chain.latest()["hash"]
    block = chain.add_block(record)

    append_log({**record, "prev_hash": prev_hash, "hash": block["hash"]})
    return {"status": "ok", "block_hash": block["hash"]}


# ============================
# READ APIs
# ============================
@app.get("/logs")
async def get_logs():
    return read_logs().to_dict(orient="records")

@app.get("/ledger")
async def get_ledger():
    return chain.to_list()

@app.get("/users")
async def get_users():
    return read_users().to_dict(orient="records")

@app.get("/")
def serve_ui():
    return FileResponse("frontend/index.html")
