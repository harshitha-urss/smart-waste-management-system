# Smart Waste Management System using AI, IoT (Software-Based), and Blockchain

A full-stack prototype that demonstrates **AI-based waste classification**,  
**software-simulated IoT bin actions**, and **blockchain-style immutable logging**.

This project is designed as an **academic + research-oriented system**, suitable for
engineering final-year projects and MS (AI / CS) profiles.

---

##  Features

-  **AI Image Classification**
  - Uses MobileNetV2 (ImageNet pretrained)
  - Classifies waste into:
    - Wet Waste
    - Dry Waste
    - Recyclable Waste
    - E-Waste
    - Cannot Be Classified (mixed/unclear)

- 🗑️ **Smart Bin Simulation (IoT – Software Based)**
  - Automatically simulates correct bin opening
  - Rejects mixed or unclear waste
  - Color-based bin logic (Green, Brown, Blue, Black)

-  **Blockchain-Style Logging**
    - Immutable, append-only ledger
    - Hash-chained logs for tamper resistance
    - Stores user actions and classification results

-  **Reward & Penalty System**
  - Tokens awarded for correct segregation
  - Rejection for incorrect or mixed waste
  - User activity tracking

-  **Web Interface**
    - Image upload from browser
    - Real-time classification results
    - Live logs display
    - Dark-mode UI

---

##  System Architecture
# Smart Waste Management System using AI, IoT (Software-Based), and Blockchain

A full-stack prototype that demonstrates **AI-based waste classification**,  
**software-simulated IoT bin actions**, and **blockchain-style immutable logging**.

This project is designed as an **academic + research-oriented system**, suitable for
engineering final-year projects and MS (AI / CS) profiles.

---

## 🚀 Features

-  **AI Image Classification**
  - Uses MobileNetV2 (ImageNet pretrained)
  - Classifies waste into:
    - Wet Waste
    - Dry Waste
    - Recyclable Waste
    - E-Waste
    - Cannot Be Classified (mixed/unclear)

-  **Smart Bin Simulation (IoT – Software Based)**
  - Automatically simulates correct bin opening
  - Rejects mixed or unclear waste
  - Color-based bin logic (Green, Brown, Blue, Black)

-  **Blockchain-Style Logging**
  - Immutable, append-only ledger
  - Hash-chained logs for tamper resistance
  - Stores user actions and classification results

-  **Reward & Penalty System**
  - Tokens awarded for correct segregation
  - Rejection for incorrect or mixed waste
  - User activity tracking

-  **Web Interface**
  - Image upload from browser
  - Real-time classification results
  - Live logs display
  - Dark-mode UI

---

##  System Architecture
User → Web UI → FastAPI Backend
↓
AI Image Model
↓
Waste Category Mapper
↓
IoT Bin Simulation (Logic)
↓
Blockchain-style Ledger Logs


---

## Tech Stack

| Layer        | Technology |
|-------------|------------|
| Frontend    | HTML, CSS, JavaScript |
| Backend     | Python, FastAPI |
| AI Model    | TensorFlow, MobileNetV2 |
| Image Proc. | Pillow |
| Logging     | CSV + SHA-256 Hashing |
| Blockchain | Custom Hash-Chained Ledger |
| Deployment  | Localhost / GitHub |

---
