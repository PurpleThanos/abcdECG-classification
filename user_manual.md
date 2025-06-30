# 📝 User Manual – ECG Classification Web App
This is a simple guide to help you run, use, and troubleshoot the ECG classification web app built with Streamlit and a trained CNN model.

---

## ⚙️ How to Run the App

1. **Install dependencies** (Python 3.10+ recommended):

    ```
    pip install -r requirements.txt
    ```

2. **Run the app** using Streamlit:

    ```
    streamlit run app.py
    ```

3. A browser will automatically open. If not, visit `http://localhost:8501`.

---

## 📂 Dataset Setup (Required Before Running)

This project uses a dataset from Kaggle:  
🔗 [ECG Images Dataset](https://www.kaggle.com/datasets/jayaprakashpondy/ecgimages)

### Steps:

1. Download and unzip the dataset from Kaggle.
2. Inside your project folder (`ecg-classification/`), create the following structure:

    ```
    ecg-classification/
    ├── app.py
    ├── ecg_model.h5
    ├── requirements.txt
    ├── README.md
    ├── user_manual.md
    ├── train/
    │   ├── Myocardial/
    │   ├── Abnormal/
    │   ├── History of MI/
    │   └── Normal/
    ├── test/
    │   ├── Myocardial/
    │   ├── Abnormal/
    │   ├── History of MI/
    │   └── Normal/
    ```

---

## 📤 Uploading ECG Images

1. On the app interface, click **“Browse files”** or drag-and-drop an ECG image.
2. Supported file formats:
    - `.jpg`
    - `.jpeg`
    - `.png`
3. Once uploaded, the model will process and display a prediction.

---

## ✅ Prediction Output

After you upload an image, the app will display:
 `Predicted Class: Myocardial / Abnormal Heatbeat / History of MI / Normal `

You will also see an option to download a report.

---

## 🧾 Generating a PDF Report 

If the app includes this feature, you will see a **Download Report** button.  
The PDF include:
- Image preview
- Prediction label
- Timestamp

This feature uses the `reportlab` library.

---

## 🛠️ Troubleshooting

| Problem                           | Solution                                                          |
|----------------------------------|-------------------------------------------------------------------|
| App doesn’t start                | Run `pip install -r requirements.txt` to install dependencies     |
| Model not found                  | Ensure `ecg_model.h5` is in the project root directory            |
| `No module named` error          | Install the missing module using `pip install <module>`          |
| Upload not working               | Check if the file format is valid (`.jpg`, `.png`)                |
| Page doesn’t load                | Try restarting Streamlit and refreshing your browser              |

---

## 👤 Author

**Leong Pui Yee**  
GitHub: https://github.com/PurpleThanos
Email: pyee009911@gmail.com

---

## ⚠️ Disclaimer

This app is for **educational use only** and not intended for medical diagnosis.  
Always consult a certified healthcare professional for real-world ECG interpretation.
