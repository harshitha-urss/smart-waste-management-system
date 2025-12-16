WET_ITEMS = [
    "vegetable", "fruit", "peel", "leftover", "eggshell", "tea",
    "banana", "apple", "orange", "rice", "bread", "flower"
]

DRY_ITEMS = [
    "paper", "newspaper", "cardboard", "carton", "envelope",
    "file", "binder", "notebook", "book", "wallet", "packet"
]

RECYCLABLE_ITEMS = [
    "plastic", "bottle", "glass", "can", "jar", "container",
    "tin", "foil", "aluminium"
]

E_WASTE_ITEMS = [
    "battery", "laptop", "computer", "phone", "charger",
    "keyboard", "mouse", "printer", "hard_disc", "pcb"
]

CATEGORY_COLOR = {
    "wet": {"name": "Green Bin"},
    "dry": {"name": "Brown Bin"},
    "recyclable": {"name": "Blue Bin"},
    "e_waste": {"name": "Black Bin"},
    "cannot_be_classified": {"name": "Rejected"}
}

def map_labels_to_category(labels):
    if not labels:
        return "cannot_be_classified"

    scores = {
        "wet": 0,
        "dry": 0,
        "recyclable": 0,
        "e_waste": 0
    }

    joined = " ".join(l.lower() for l in labels)

    for kw in WET_ITEMS:
        if kw in joined:
            scores["wet"] += 1

    for kw in DRY_ITEMS:
        if kw in joined:
            scores["dry"] += 1

    for kw in RECYCLABLE_ITEMS:
        if kw in joined:
            scores["recyclable"] += 1

    for kw in E_WASTE_ITEMS:
        if kw in joined:
            scores["e_waste"] += 1

    # ---- DECISION LOGIC ----

    # If absolutely nothing matched
    if max(scores.values()) == 0:
        return "cannot_be_classified"

    # Priority-based tie breaking (real-world logic)
    PRIORITY = ["e_waste", "recyclable", "dry", "wet"]

    best_score = max(scores.values())

    for cat in PRIORITY:
        if scores[cat] == best_score:
            return cat
