## **About**
- End-to-end **web app for heart disease risk prediction** using a **Logistic Regression model** built with Flask.  
- Classifies individuals into **high/low heart disease risk** categories based on multiple medical parameters.  
- Uses the **Kaggle Heart Disease Dataset** containing **1028 samples** with clinical and lifestyle-related attributes.  
- Includes **data preprocessing** (scaling and encoding) for accurate and consistent predictions.  
- 🎬 **Watch the project demo:** [HART on YouTube](https://www.youtube.com/watch?v=Qbb6hJWcU1s)

---

## **Dataset Overview**
- **Dataset Name:** Heart Disease Dataset (Kaggle)  
- **Number of Records:** 1028  
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
- **Target:** High risk vs Low risk of heart disease (binary classification)  
- **Source:** [Kaggle Heart Disease Dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)

---

## **Model Overview**

| Parameter                     | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| **Model Type**                 | Logistic Regression                                                        |
| **Objective**                  | Binary classification (high/low risk)                                      |
| **Class Imbalance Handling**   | Class weights applied (`class_weight={1:1.6}`) to emphasize high-risk cases |
| **Scaling**                    | StandardScaler applied to numerical features                               |
| **Encoding**                   | LabelEncoder applied to categorical features                               |
| **Train/Test Split**           | 80/20                                                                      |
| **Evaluation Metrics**         | Accuracy, Precision, Recall, F1-score, ROC-AUC                              |
| **Train Accuracy**             | 85%                                                                         |
| **Test Accuracy**              | 80%                                                                         |
| **Cross-Validation Accuracy**  | 81.3% (5-fold CV on training set)                                          |
| **ROC-AUC**                    | 0.83                                                                        |

---

## **Key Features**
- Input **medical features** via a simple web form  
- Predict **heart disease risk (high/low)** instantly  
- **Preprocessed pipeline** ensures consistent input scaling and encoding  
- **Class imbalance handled** to prioritize detection of high-risk cases  
- **Explainable predictions:** top features include `thalach` (max heart rate), `chol` (cholesterol), and `age`  
- Built with **Flask backend** and lightweight **HTML frontend**  
- Architecture allows **future deployment** on cloud platforms (AWS, Render, Heroku) and inclusion of additional ML models  

---

## **Tech Stack**
- **Backend:** Flask (Python)  
- **Model:** Logistic Regression (scikit-learn)  
- **Data Processing:** NumPy, Pandas, Joblib, StandardScaler, LabelEncoder  
- **Visualization:** Matplotlib, Seaborn  
- **Frontend:** HTML, CSS  
- **Deployment:** Local (demo-ready architecture for cloud deployment)  

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
