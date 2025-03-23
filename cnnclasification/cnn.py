import streamlit as st
from PIL import Image
from transformers import ViTFeatureExtractor, ViTForImageClassification
import torch

# Load model and processor
@st.cache_resource
def load_model():
    model_name = "google/vit-base-patch16-224"  # Model trained on ImageNet
    model = ViTForImageClassification.from_pretrained(model_name)
    processor = ViTFeatureExtractor.from_pretrained(model_name)
    return model, processor

# Prediction function
def classify(image, model, processor):
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    predicted_class = outputs.logits.argmax().item()
    return model.config.id2label[predicted_class]  # Returns human-readable label

# Streamlit UI
st.title("Simple Hugging Face Image Classifier")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    model, processor = load_model()
    prediction = classify(image, model, processor)
    
    st.subheader(f"Prediction: {prediction}")
