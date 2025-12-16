# ♻️ Smart Waste Management System using AI, IoT (Software-Based) & Blockchain

An end-to-end intelligent waste segregation system that classifies waste images using deep learning, simulates IoT-based smart bin operations, and records all actions using a blockchain-inspired immutable ledger.

🔗 **Live Demo:**  
https://smart-waste-management-system-bpyt.onrender.com/

> ⚠️ Hosted on Render free tier. Initial load may take 30–60 seconds.

---

## 📌 Problem Statement

Improper waste segregation leads to environmental pollution, inefficient recycling, and increased landfill usage. Manual segregation is unreliable and not scalable.

This project proposes an **AI-driven smart waste management system** that:
- Automatically classifies waste using images
- Rejects mixed or unclear waste
- Simulates IoT-controlled waste bins
- Maintains transparent logs using blockchain principles
- Encourages correct segregation via a reward mechanism

---

## Objectives

- Automate waste classification using deep learning
- Handle real-world ambiguity (mixed waste)
- Integrate AI, IoT (software-based), and Blockchain
- Build a deployable, production-ready system
- Promote responsible waste disposal

---

## System Workflow

1. User uploads an image via the web interface  
2. AI model predicts ImageNet labels  
3. Semantic mapper converts labels into waste categories  
4. Decision engine:
   - Valid category → corresponding bin opens
   - Mixed/unclear → rejected
5. Action is logged in a blockchain-style ledger  
6. User is rewarded or penalized accordingly  

---

## Waste Categories Supported

| Category | Examples |
|--------|---------|
| **Wet Waste** | Food waste, fruit peels, vegetables |
| **Dry Waste** | Paper, newspaper, cardboard |
| **Recyclable** | Plastic bottles, glass, aluminium cans |
| **E-Waste** | Chargers, laptops, keyboards |
| **Cannot be Classified** | Mixed or unclear waste |

> Mixed waste is intentionally rejected to promote proper segregation.

---

## AI Model

- **Model:** MobileNetV2 (pre-trained on ImageNet)
- **Framework:** TensorFlow / Keras
- **Input:** RGB image (224 × 224)
- **Output:** Top-K ImageNet predictions
- **Mapping:** Keyword-based semantic scoring
- **Fallback:** Rejects low-confidence or ambiguous results

---

## Blockchain (Software-Based)

A lightweight blockchain-inspired ledger ensures transparency and immutability.

Each record includes:
- Timestamp
- User ID
- Waste item
- Predicted category
- Status
- Previous hash
- Current hash

This prevents tampering and provides accountability.

---

## IoT Integration (Simulated)

- Software-based IoT simulation
- Bin opens based on classification
- Color-coded bins:
  - 🟢 Green – Wet
  - 🟤 Brown – Dry
  - 🔵 Blue – Recyclable
  - ⚫ Black – E-Waste

Can be extended to real IoT hardware.

---

## Tech Stack

### Backend
- Python
- FastAPI
- TensorFlow / Keras
- NumPy, Pandas
- Uvicorn

### Frontend
- HTML
- CSS
- JavaScript (Vanilla)

### Deployment
- Render
- GitHub

---

## 🚀 Live Deployment

🌍 Public URL:  
https://smart-waste-management-system-bpyt.onrender.com/

- AI inference runs on server
- Frontend served via FastAPI
- Globally accessible

---
## Future Scope
- Train a dedicated waste classification model for higher accuracy.
- Integrate real IoT hardware such as smart bins and sensors.
- Implement blockchain smart contracts for secure data handling.
- Develop a mobile application for public use.
- Deploy the system for smart city and municipal waste management.

---

## 📄 License
This project is licensed under the MIT License.

---

## Author
**HARSHITHA M V**  
AI & ML Engineering Student  
