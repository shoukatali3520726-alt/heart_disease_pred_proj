# ❤️ Heart Disease Prediction Using Machine Learning

## Project Overview

**Heart Disease Prediction** is a Machine Learning project that predicts the possibility of heart disease from patient health-related features. It includes a Jupyter Notebook for data analysis and model development, plus a Streamlit application for making predictions.

This project is intended for learning and demonstration purposes only.

## Project Files

```text
heart_disease_pred_proj/
├── app1.py                 # Streamlit application
├── heart_disease.ipynb     # Data analysis and model development notebook
├── heart.csv               # Dataset
├── KNN_heart.pkl           # Trained K-Nearest Neighbors model
├── scaler.pkl              # Saved feature scaler
├── columns.pkl             # Saved feature-column information
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## Machine Learning Model

- **Algorithm:** K-Nearest Neighbors (KNN)
- **Task:** Binary classification
- **Dataset:** `heart.csv`
- **Saved artifacts:** `KNN_heart.pkl`, `scaler.pkl`, and `columns.pkl`

The scaler and saved column information help the application prepare input features in the format expected by the trained model.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib / Python pickle files
- Jupyter Notebook
- Matplotlib and Seaborn (for data visualization, if used in the notebook)

## Setup and Run Locally

### 1. Clone the repository

Replace `YOUR-USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR-USERNAME/heart_disease_pred_proj.git
```

### 2. Move into the project folder

```bash
cd heart_disease_pred_proj
```

### 3. (Recommended) Create and activate a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the Streamlit app

```bash
streamlit run app1.py
```

Streamlit will show a local URL in the terminal. Open that URL in your browser.

### 6. Open the notebook (optional)

```bash
jupyter notebook
```

Then open `heart_disease.ipynb`.

## Important Notes

- Keep `KNN_heart.pkl`, `scaler.pkl`, and `columns.pkl` in the same project directory as `app1.py`, unless the code uses different file paths.
- The saved model files should be loaded with compatible versions of Scikit-learn and related libraries. If you get a model-loading warning or error, check the versions used when the `.pkl` files were created.
- Make sure the column order and preprocessing in the app match those used when training the model.
- Do not upload private information, API keys, or sensitive patient data.

## Disclaimer

This application is for educational purposes only. It is **not** a medical device and must not be used to diagnose heart disease or replace advice from a qualified healthcare professional.

## Author

**Shoukat Ali**  
Machine Learning Student | Aspiring AI Engineer

If you find this project useful, feel free to star the repository on GitHub.
