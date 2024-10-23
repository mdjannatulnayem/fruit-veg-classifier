import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the TensorFlow Lite model
model_path = "vegModels.tflite"
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Load class labels from the text file
with open('labels.txt', 'r') as file:
    class_labels = file.read().splitlines()

# Streamlit Sidebar: Developer Info and Project Overview
st.sidebar.title("Fruit & Vegetable Classifier 🍎🥕")
st.sidebar.markdown("""
**Version:** 1.0.0  
**Developer:** Akash Ghosh  
**GitHub:** [Github](https://github.com/akashghosh20)  
**Email:** ag1229222@gmail.com
""")

# Sidebar Project Overview
st.sidebar.header("Project Overview")
st.sidebar.markdown("""
The **Fruit and Vegetable Classifier** is a deep learning-based web app that classifies images of fruits and vegetables.  
- **Upload an Image:** Upload a picture of fruits or vegetables and the app will predict the correct class.
- **Efficient Inference:** The model uses TensorFlow Lite for fast image classification.
- **Trained on:** A curated subset of the Fruits-360 dataset, which includes a wide variety of categories:
  - Apples (Golden, Red, Granny Smith, etc.)
  - Bananas, Blueberries, Grapes, Mangoes
  - Carrots, Cauliflower, Eggplant, Ginger
  - Peppers (Red, Green, Yellow) and more...
""")

# Sidebar: Key Features
st.sidebar.header("Key Features")
st.sidebar.info("""
- **Upload & Classify:** Simply upload an image of fruits or vegetables and get a prediction.
- **Fast Inference:** Uses TensorFlow Lite for efficient image processing.
- **Visualize Predictions:** A bar chart shows the model's confidence in each class.
""")

# Streamlit UI: Improved Design
st.markdown("""
<style>
    .main-title {
        font-family: 'Arial Black', sans-serif;
        font-size: 50px;
        color: #4CAF50;
        text-align: center;
        margin-top: 30px;
    }
    .sub-title {
        font-size: 20px;
        color: #6c757d;
        text-align: center;
        margin-bottom: 30px;
    }
    .image-display {
        text-align: center;
    }
    img {
        border-radius: 15px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease-in-out;
    }
    img:hover {
        transform: scale(1.02);
    }
    .stButton>button {
        background-color: #007BFF;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    .result {
        font-size: 24px;
        font-weight: bold;
        color: #007bff;
        text-align: center;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Fruit and Vegetable Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Upload an image and let me classify it!</div>', unsafe_allow_html=True)

# File uploader
uploaded_image = st.file_uploader('', type=['jpg', 'jpeg', 'png'], label_visibility="collapsed")

if uploaded_image is not None:
    # Preprocess the image
    image = Image.open(uploaded_image)
    image = image.resize((224, 224))
    image_np = np.array(image)
    image_np = (image_np / 255.0).astype(np.float32)
    image_np = image_np[np.newaxis, ...]

    # Run inference
    interpreter.set_tensor(input_details[0]['index'], image_np)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]['index'])

    # Predicted class
    predicted_class_index = np.argmax(output)
    predicted_label = class_labels[predicted_class_index]

    # Display uploaded image
    st.markdown('<div class="image-display">', unsafe_allow_html=True)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Display result
    st.markdown(f'<div class="result">Predicted Class: {predicted_label}</div>', unsafe_allow_html=True)
else:
    # Placeholder message before image upload
    st.markdown('<div class="upload-area">Please upload an image to classify!</div>', unsafe_allow_html=True)
