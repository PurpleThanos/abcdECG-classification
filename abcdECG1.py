#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Inject custom CSS for light theme and colors
st.markdown("""
    <style>
        /* Set background color */
        body, .stApp {
            background-color: #ffffff;
            color: #185eaf;
        }

        /* Set text color for headers and markdown */
        h1, h2, h3, h4, h5, h6, p, div, span {
            color: #185eaf !important;
        }

        /* Button styles */
        .stButton>button {
            background-color: #185eaf;
            color: #ffffff;
            border: none;
        }
        .stButton>button:hover {
            background-color: #9f2d2a;
            color: #ffffff;
        }

        /* Warning box styling */
        .stAlert {
            background-color: #ffecec;
            color: #9f2d2a !important;
        }

        /* File uploader text */
        .css-1cpxqw2, .css-9ycgxx {
            color: #185eaf !important;
        }
    </style>
""", unsafe_allow_html=True)


# Load model
model = load_model("ecg_model.h5")

# Class labels
class_names = [
    'Myocardial Infarction',
    'History of MI',
    'Abnormal Heartbeat',
    'Normal'
]

# Prediction function
def predict(image):
    image = image.convert("RGB")
    image = image.resize((224, 224))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    preds = model.predict(img_array)[0]
    return preds

# Streamlit UI
st.title("🩺 ECG Image Classifier")
st.write("Upload an ECG image and get a prediction!")

uploaded_file = st.file_uploader("Choose an ECG image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded ECG", use_container_width=True)

    st.write("Classifying...")
    predictions = predict(image)
    top_class_index = np.argmax(predictions)
    top_class = class_names[top_class_index]
    confidence = predictions[top_class_index]

    # Show prediction and confidence
    st.subheader(f"❤️ Prediction: {top_class}")
    
    # Threshold warning
    if confidence < 0.6:
        st.warning("Model is not confident enough to make a reliable prediction.")

    st.write("### Confidence:")
    for i in range(len(class_names)):
        st.write(f"- **{class_names[i]}**: {predictions[i]*100:.2f}%")

