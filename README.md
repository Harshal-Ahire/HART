## **About**
- End-to-end **web app for heart disease risk prediction** using a **Logistic Regression model** built with Flask.  
- Classifies individuals into **high/low heart disease risk** categories based on multiple medical parameters.  
- Uses the **Kaggle Heart Disease Dataset** containing clinical and lifestyle-related attributes.  
- Includes **data preprocessing** (scaling and encoding) for accurate and consistent predictions.  
- 🎬 **Watch the project demo:** [HART on YouTube](https://www.youtube.com/watch?v=Qbb6hJWcU1s)

--

## **Dataset Overview**
- **Dataset Name:** Heart Disease Dataset (Kaggle)  
- **Number of Records:** ~303 entries  
- **Features:**  
  - Age  
  - Sex  
  - Chest pain type (cp)  
  - Resting blood pressure (trestbps)  
  - Cholesterol level (chol)  
  - Fasting blood sugar (fbs)  
  - Resting ECG results (restecg)  
  - Maximum heart rate achieved (thalach)  
  - Exercise-induced angina (exang)  
  - ST depression (oldpeak)  
  - Slope of peak exercise ST segment (slope)  
  - Number of major vessels (ca)  
  - Thalassemia (thal)  
- **Target:** Presence or absence of heart disease (binary classification)  
- **Source:** [Kaggle Heart Disease Dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)

---

## **Model Overview**

| Parameter                     | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| **Model Type**                 | Logistic Regression                                                        |
| **Objective**                  | Binary classification (high/low risk)                                      |
| **Optimizer**                  | Gradient Descent (via scikit-learn implementation)                         |
| **Scaling**                    | StandardScaler applied to numerical features                               |
| **Encoding**                   | LabelEncoder for categorical variables                                     |
| **Train/Test Split**           | 80/20                                                                      |
| **Evaluation Metric**          | Accuracy, Precision, Recall, F1-score                                      |

---

## **Key Features**
- Input **medical features** via a simple web form  
- Predict **heart disease risk (high/low)** instantly  
- **Preprocessed pipeline** ensures consistent input scaling and encoding  
- Built with **Flask backend** and a lightweight **HTML frontend**  
- Clean and interpretable prediction flow suitable for demonstrations  

---

## **Tech Stack**
- **Backend:** Flask (Python)  
- **Model:** Logistic Regression (scikit-learn)  
- **Data Processing:** NumPy, Joblib  
- **Frontend:** HTML, CSS  
- **Deployment:** Local (demo-ready architecture for Render/Streamlit integration)  

---

## **Installation and Setup**
Please refer to the `requirements.txt` file for a list of dependencies required to run the project locally.

---

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.

---

## **Contributing**
If you'd like to contribute to this project, please follow these steps:  
1. Fork the repository.  
2. Create a new branch for your changes.  
3. Submit a pull request with a clear description of the changes you've made.

---

## **Disclaimer**
- This project is for **educational and demonstration purposes only**.  
- **Not intended for clinical or diagnostic use**.  
