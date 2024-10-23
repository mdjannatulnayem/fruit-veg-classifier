🍎🍉 Fruit and Vegetable Classifier 🍇🥕
Version: 1.0.0

https://drive.google.com/file/d/1ItqxX1xDQzumJerZ7Z9cUDHDqLSF1Izy/view?usp=sharing


Overview

The Fruit and Vegetable Classifier is a web-based deep learning application that classifies images of fruits and vegetables. Powered by TensorFlow Lite, this app allows users to upload images and predict the type of fruit or vegetable in the image. It is a practical demonstration of how machine learning models can be deployed efficiently for real-world image classification.

This app is built with a clean and modern UI using Streamlit. The classifier was trained using the Fruits-360 dataset, which contains a wide range of categories of fruits and vegetables (131 categories).


Features

Upload & Classify: Upload an image (JPEG, PNG) of a fruit or vegetable, and the AI will classify it.
Fast Inference: Powered by TensorFlow Lite, providing efficient and quick image classification.
User-friendly UI: Intuitive and attractive interface designed using Streamlit with custom HTML/CSS styling.
Prediction Visualization: Displays prediction results and optional bar chart of classification probabilities.
Developer Info Sidebar: Information like the developer's GitHub, LinkedIn, and email provided for easy contact.


Demo

You can test this app by uploading an image of fruits or vegetables, and it will return a classification result based on the model’s predictions.


Dataset

This model was trained on the Fruits-360 dataset, a collection of high-quality images of fruits, vegetables, and nuts. The dataset is diverse, containing categories such as:

Apples (Golden, Red, Granny Smith, etc.)
Bananas (Yellow, Red)
Blueberries, Cherries, Grapes, Mangoes
Carrots, Cauliflower, Eggplant, Ginger
Peppers (Red, Green, Yellow)
You can download the Fruits-360 dataset directly from this link:

[Download Fruits-360 Dataset](https://github.com/Horea94/Fruit-Images-Dataset)

Make sure to use the test folder for classification tasks.

Getting Started
Prerequisites
Before you begin, make sure you have the following installed:

Python 3.x
Streamlit
TensorFlow
Required Python libraries (can be installed via requirements.txt)
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/fruit-veg-classifier.git
cd fruit-veg-classifier
Create a virtual environment (optional but recommended):
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required Python packages:
bash
Copy code
pip install -r requirements.txt
Download and extract the dataset:
Go to the Fruits-360 Dataset, download the ZIP file, and extract it into the project folder. Specifically, use the test folder for the classification task.

bash
Copy code
unzip fruits-360-dataset.zip -d dataset/
Ensure the dataset's test folder contains subdirectories with images of various fruits and vegetables.

Download the TensorFlow Lite model:
Place your vegModels.tflite model file in the root of the project directory.

Download the class labels:
Ensure the labels.txt file is also in the root directory. This file contains the names of the classes (fruit/vegetable categories).

Running the App
Run the Streamlit app:

bash
Copy code
streamlit run main.py
Upload an Image:
After the app launches, you will be prompted to upload an image of a fruit or vegetable. Once uploaded, the app will classify the image and display the prediction.

Project Structure
bash
Copy code
fruit-veg-classifier/
│
├── dataset/               # Contains extracted dataset from ZIP
│   ├── test/              # Images for classification
├── vegModels.tflite       # TensorFlow Lite model for classification
├── labels.txt             # Class labels for prediction
├── main.py                # Main Streamlit app file
├── README.md              # Project README file
└── requirements.txt       # Python dependencies
Customization
Styling
The UI for this project is styled using HTML and CSS embedded within Streamlit's st.markdown() method. You can further customize the appearance by editing the styles in the main.py file, specifically within the st.markdown() sections for the main page and sidebar.

Future Improvements
Add more categories: Expand the model to classify more types of fruits and vegetables.
Confidence visualization: Add a feature to display a confidence chart for predictions, providing users with more insights into the AI's certainty.
Contact
For any questions or suggestions, feel free to contact the developer:

Email: ag1229222@gmail.com
This project was developed for educational purposes as a demonstration of TensorFlow Lite and Streamlit integration for machine learning applications.
