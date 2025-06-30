# 🩺 ECG Classification Web App

This is a deep learning web application that classifies ECG images into different heart condition categories using a Convolutional Neural Network (CNN). The app is built using **Streamlit** and is designed for users to easily upload ECG images and get real-time predictions.

---

## 📌 Features

- Upload `.jpg` or `.png` ECG images
- Predict heart conditions using a trained CNN model
- Generate a diagnosis PDF report
- User-friendly Streamlit interface

---

## 🧠 Model Details

- Trained using a CNN with Keras/TensorFlow
- Based on image data from a publicly available ECG dataset
- Saved model: `ecg_model.h5`

---

## 📂 Dataset

The dataset used for training and testing is from Kaggle:  
🔗 [ECG Images Dataset by Jayaprakash Pondy](https://www.kaggle.com/datasets/jayaprakashpondy/ecgimages)

**How to use it:**

1. Go to the Kaggle dataset link above.
2. Download the dataset ZIP file (requires a Kaggle account).
3. Extract the ZIP file.
4. Copy the `train/` and `test/` folders into the root directory of this project.

