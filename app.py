from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('best_model.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('medical.html')

@app.route('/predict', methods=['POST'])
def death_event():
    age = int(request.form.get('age'))
    anaemia = int(request.form.get('anaemia'))
    creatinine_phosphokinase = int(request.form.get('creatinine_phosphokinase'))
    diabetes = int(request.form.get('diabetes'))
    ejection_fraction = int(request.form.get('ejection_fraction'))
    high_blood_pressure = int(request.form.get('high_blood_pressure'))
    platelets = float(request.form.get('platelets'))
    serum_creatinine = float(request.form.get('serum_creatinine'))
    serum_sodium = int(request.form.get('serum_sodium'))
    sex = int(request.form.get('sex'))
    smoking = int(request.form.get('smoking'))
    time = int(request.form.get('time'))

    input_data = np.array([age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction,
                           high_blood_pressure, platelets, serum_creatinine, serum_sodium,
                           sex, smoking, time]).reshape(1, -1)

    result = model.predict(input_data)[0]

    if result == 0:
        outcome = "✅ Safe Signal: The model predicts the patient is likely to survive."
    else:
        outcome = "⚠️ Risk Alert: The model predicts the patient might die."

    return render_template('medical.html', result=outcome)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
