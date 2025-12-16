from PIL import Image, ImageDraw, ImageFont
import os
import random

OUTPUT_DIR = "test_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

CATEGORIES = {
    "wet": "GREEN BIN",
    "dry": "BROWN BIN",
    "recyclable": "BLUE BIN",
    "e_waste": "BLACK BIN",
    "mixed": "MIXED / UNKNOWN"
}

TOTAL_IMAGES = 250

for i in range(1, TOTAL_IMAGES + 1):
    category = random.choice(list(CATEGORIES.keys()))

    img = Image.new("RGB", (224, 224), color=(240, 240, 240))
    draw = ImageDraw.Draw(img)

    text = f"{category.upper()}\nTEST IMAGE"
    draw.text((40, 90), text, fill=(0, 0, 0))

    filename = f"{category}_{i:03}.png"
    img.save(os.path.join(OUTPUT_DIR, filename))

print(f"✅ Generated {TOTAL_IMAGES} test images in '{OUTPUT_DIR}/'")
