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

- Trained using a CNN with Keras
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

---

## 🚀 How to Run the App

1. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

3. The app will open in your browser at `http://localhost:8501`

---

## 🧾 Report Generation

The app allows users to download a **PDF report** containing:
- Uploaded ECG image
- Predicted condition
- Timestamp

---

## 📖 Documentation

- 📘 [User Manual](user_manual.md)

---

## 🧑‍💻 Author

**Leong Pui Yee**  
GitHub: [https://github.com/PurpleThanos](https://github.com/PurpleThanos)  
Email: [pyee009911@gmail.com]

---

## ⚠️ Disclaimer

This tool is for **educational and demonstration purposes only**. It is not approved for clinical use. Always consult a medical professional for official diagnoses.

---

## 📄 License

MIT License – feel free to use, fork, and contribute.

