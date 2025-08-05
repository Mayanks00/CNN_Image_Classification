# app.py : Streamlit Web App for CNN Image Classification

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load trained model
model = tf.keras.models.load_model("cnn_cifar10_model.h5")

# CIFAR-10 class labels
class_names = ['Airplane','Automobile','Bird','Cat','Deer',
               'Dog','Frog','Horse','Ship','Truck']

# Streamlit App UI
st.title("🖼️ CIFAR-10 Image Classifier")
st.write("Upload an image (32x32 or larger) to classify it into one of 10 classes.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])

if uploaded_file is not None:
    # Show uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", width=150)
    
    # Preprocess image
    img = img.resize((32,32))
    img_array = np.array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    prediction = model.predict(img_array)
    pred_class = class_names[np.argmax(prediction)]

    st.write(f"🎯 **Predicted Class:** {pred_class}")
