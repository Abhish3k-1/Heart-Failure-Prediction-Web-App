# ❤️ Heart Failure Prediction using Machine Learning

This project is a machine learning web app that predicts the likelihood of a patient's death due to heart failure based on various clinical features.

## 🚀 Features

- Preprocessing with `StandardScaler`
- Predicts patient risk based on 12 clinical features
- Simple Flask web app frontend
- Clean UI using HTML & CSS
- Ready for deployment

## 🧠 Model Details

- Dataset: [Heart Failure Clinical Records Dataset]
- Preprocessing: `StandardScaler`
- Accuracy: ~90% after hyperparameter tuning
- Serialization: Model is saved using `pickle` and `gzip`

## 🧪 Input Features

1. Age
2. Anaemia (0 or 1)
3. Creatinine Phosphokinase
4. Diabetes (0 or 1)
5. Ejection Fraction
6. High Blood Pressure (0 or 1)
7. Platelets
8. Serum Creatinine
9. Serum Sodium
10. Sex (0 for female, 1 for male)
11. Smoking (0 or 1)
12. Time (Follow-up days)

## 🛠 Tech Stack

- Python 3.x
- Flask
- HTML, CSS
- scikit-learn, pandas, numpy, matplotlib
- VS Code

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/heart-failure-predictor.git
cd heart-failure-predictor

# (Optional but recommended) Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
