import joblib
from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__)

# Load the pre-trained model, scaler, and label encoder
model = joblib.load('model/log_reg_model.pkl')
scaler = joblib.load('model/scaler.pkl')
le = joblib.load('model/label_encoder.pkl')

@app.route('/')
def home():
    # Ensure prediction_text is always set, even if it's an empty string
    prediction_text = ""  # Default value when there's no prediction
    return render_template('index.html', prediction_text=prediction_text)

@app.route('/predict', methods=['POST'])
def predict():
    # Extract input data from the form
    cp = int(request.form['cp'])
    thalach = int(request.form['thalach'])
    chol = int(request.form['chol'])
    exang = int(request.form['exang'])
    ca = int(request.form['ca'])
    age = int(request.form['age'])
    sex = int(request.form['sex'])
    trestbps = int(request.form['trestbps'])
    oldpeak = float(request.form['oldpeak'])

    # Apply label encoding to categorical features (cp, exang, etc.)
    cp = le.transform([cp])[0]  # Transform the cp value
    exang = le.transform([exang])[0]  # Transform exang if applicable

    # Create a list for the numerical features (do not include oldpeak here)
    numerical_features = [thalach, chol, age, trestbps]  # Only these will be scaled
    categorical_features = [cp, exang, ca, sex]  # These are categorical features only

    # Apply scaling only to the 4 numerical features using the saved scaler
    numerical_features_scaled = scaler.transform([numerical_features])

    # Combine the scaled numerical features with categorical features into one input list
    input_data = np.concatenate([numerical_features_scaled[0], categorical_features, [oldpeak]])

    # Reshape to match the expected input shape for the model
    input_data = input_data.reshape(1, -1)

    # Make prediction
    prediction = model.predict(input_data)

    # Display the prediction result
    if prediction == 0:
        result = "Low Risk of Heart Disease"
    else:
        result = "High Risk of Heart Disease"

    # Return the prediction result to be displayed on the page
    return render_template('index.html', prediction_text=f"Evaluation: {result}")

if __name__ == "__main__":
    app.run(debug=True)
