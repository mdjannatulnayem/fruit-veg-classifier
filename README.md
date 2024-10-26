
# 🍎🍉 Fruit and Vegetable Classifier 🍇🥕
**Version**: 1.0.0

![UI of Fruit and Vegetable Classifier](https://drive.google.com/uc?export=view&id=1ItqxX1xDQzumJerZ7Z9cUDHDqLSF1Izy)

```markdown

## 🌟 Overview
The **Fruit and Vegetable Classifier** is a web-based deep learning application that classifies images of fruits and vegetables. Powered by **TensorFlow Lite**, this app enables users to upload images and predict the type of fruit or vegetable displayed. It demonstrates how machine learning models can be effectively deployed for real-world image classification.

This app is crafted with a clean and modern UI using **Streamlit** and is trained using the **Fruits-360 dataset**, encompassing a variety of 131 fruit and vegetable categories.

---

## 🔥 Features
- **Upload & Classify**: Upload an image (JPEG, PNG) of a fruit or vegetable, and the AI will identify it.
- **Fast Inference**: Leverages TensorFlow Lite for efficient and rapid image classification.
- **User-friendly UI**: Built with an attractive interface using Streamlit, enhanced with custom HTML/CSS styling.
- **Prediction Visualization**: Displays prediction results, with an optional bar chart for classification probabilities.
- **Developer Info Sidebar**: Quick links for GitHub, LinkedIn, and email for easy contact.

---

## 🎬 Demo
Upload an image of a fruit or vegetable to test the classifier, which will return a classification based on the model's predictions.

---

## 📊 Dataset
This model is trained on the **Fruits-360 dataset**, a comprehensive collection of high-quality fruit, vegetable, and nut images. The dataset includes categories such as:

- Apples (Golden, Red, Granny Smith, etc.)
- Bananas (Yellow, Red)
- Blueberries, Cherries, Grapes, Mangoes
- Carrots, Cauliflower, Eggplant, Ginger
- Peppers (Red, Green, Yellow)

 ```

Download the dataset here:

[Download Fruits-360 Dataset](https://github.com/Horea94/Fruit-Images-Dataset)

> **Note**: Use the `test` folder for classification tasks.

---

## 🚀 Getting Started

### Prerequisites
Ensure the following are installed:

- **Python 3.x**
- **Streamlit**
- **TensorFlow**
- **Required Python libraries** (listed in `requirements.txt`)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/akashghosh20/fruit-veg-classifier.git
   cd fruit-veg-classifier
  

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download and extract the dataset**:
   Download the Fruits-360 ZIP file and extract it into the project folder, specifically using the `test` folder for classification tasks.
   ```bash
   unzip fruits-360-dataset.zip -d dataset/
   ```

5. **Add the TensorFlow Lite model and labels**:
   - Place `vegModels.tflite` (TensorFlow Lite model) in the root directory.
   - Ensure `labels.txt` (class labels) is also in the root directory.

---

## 🖥️ Running the App
1. **Launch the Streamlit app**:
   ```bash
   streamlit run main.py
   ```

2. **Upload an Image**:
   Once the app is running, upload an image of a fruit or vegetable. The app will classify the image and display the prediction.

---

## 📁 Project Structure
```plaintext
fruit-veg-classifier/
│
├── dataset/            # Contains extracted dataset from ZIP
│   └── test/           # Images for classification
├── vegModels.tflite    # TensorFlow Lite model for classification
├── labels.txt          # Class labels for prediction
├── main.py             # Main Streamlit app file
├── README.md           # Project README file
└── requirements.txt    # Python dependencies
```

---

## 🎨 Customization

### Styling
The UI of this project is styled using HTML and CSS embedded within Streamlit's `st.markdown()` method. To customize the appearance further, edit the styles within `main.py`, especially in the `st.markdown()` sections for the main page and sidebar.

---

## 🚀 Future Improvements
- **Expand Categories**: Increase the range of fruits and vegetables the model can classify.
- **Confidence Visualization**: Add a confidence chart for predictions, providing users more insight into the model's certainty.

---

## 👤 Contact
For any questions or suggestions, please reach out:

- **Email**: ag1229222@gmail.com

This project was created as an educational demonstration of TensorFlow Lite and Streamlit integration for machine learning applications.

---
