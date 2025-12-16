# backend/schemas.py
from pydantic import BaseModel
from typing import Optional

class IoTData(BaseModel):
    device_id: str
    timestamp: Optional[float]
    action: str
    meta: Optional[dict] = None

class UploadResponse(BaseModel):
    predicted_category: str
    top_labels: list
    awarded_tokens: int
    message: str
