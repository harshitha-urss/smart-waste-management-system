# backend/ai_model.py

from tensorflow.keras.applications import mobilenet_v2
from tensorflow.keras.preprocessing import image as kimage
import numpy as np

_model = None

def load_model():
    global _model
    if _model is None:
        _model = mobilenet_v2.MobileNetV2(weights="imagenet")
    return _model

def preprocess(pil_img):
    img = pil_img.resize((224, 224))
    x = kimage.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    return mobilenet_v2.preprocess_input(x)

def predict_labels(pil_img, topk=7):
    model = load_model()

    x = preprocess(pil_img)
    preds = model.predict(x)

    decoded = mobilenet_v2.decode_predictions(preds, top=topk)[0]
    labels = [label for (_, label, prob) in decoded]

    return labels, decoded
