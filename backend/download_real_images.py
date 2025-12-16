from bing_image_downloader import downloader
import os

BASE_DIR = "demo_images"

DATASET = {
    "wet": [
        "banana waste",
        "food waste kitchen",
        "vegetable peels waste"
    ],
    "dry": [
        "paper waste",
        "cardboard waste",
        "newspaper waste"
    ],
    "recyclable": [
        "plastic bottle waste",
        "glass bottle waste",
        "aluminium can waste"
    ],
    "e_waste": [
        "old laptop electronic waste",
        "mobile charger electronic waste",
        "computer keyboard electronic waste"
    ],
    "cannot_be_classified": [
        "mixed garbage waste",
        "trash pile mixed waste",
        "landfill waste mixed"
    ]
}

IMAGES_PER_QUERY = 20  # 3 queries × 20 = 60 images per class

os.makedirs(BASE_DIR, exist_ok=True)

for category, queries in DATASET.items():
    category_dir = os.path.join(BASE_DIR, category)
    os.makedirs(category_dir, exist_ok=True)

    for q in queries:
        downloader.download(
            q,
            limit=IMAGES_PER_QUERY,
            output_dir=category_dir,
            adult_filter_off=True,
            force_replace=False,
            timeout=60
        )

print("✅ Real waste images downloaded & organised successfully!")
