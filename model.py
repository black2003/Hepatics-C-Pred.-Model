import streamlit as st
import pandas as pd
import joblib

# Load your trained model
model = joblib.load(r"C:\Users\asus\Downloads\PDS\Logistic Regression.pkl")

# Create a Streamlit web app
st.title("Hepatitis C Prediction")

st.write("Enter the required information to predict Hepatitis C.")

# User input
st.sidebar.header("User Input")
age = st.sidebar.slider("Age", 1, 100, 25)
sex = st.sidebar.radio("Sex", ("male", "female"))
ALB = st.sidebar.slider("ALB", 1, 100, 25)
ALP = st.sidebar.slider("ALP", 1, 100, 25)
ALT = st.sidebar.slider("ALT", 1, 100, 25)
AST = st.sidebar.slider("AST", 1, 100, 25)
BIL = st.sidebar.slider("BIL", 1, 100, 25)
CHE = st.sidebar.slider("CHE", 1, 100, 25)
CHOL = st.sidebar.slider("CHOL", 1, 100, 25)
CREA = st.sidebar.slider("CREA", 1, 100, 25)
GGT = st.sidebar.slider("GGT", 1, 100, 25)
PROT = st.sidebar.slider("PROT", 1, 100, 25)
# Add more input fields for other features as needed

# Feature preprocessing (ensure it's the same as in your training data)

# Predict
if st.button("Predict"):
    input_data = pd.DataFrame({
        "Age": [age],
        "Sex": [sex],
        "ALB": [ALB],
        "ALP": [ALP],
        "ALT": [ALT],
        "AST": [AST],	
        "BIL": [BIL],
        "CHE": [CHE],
        "CHOL":[CHOL],
        "CREA":[CREA],
        "GGT": [GGT],	
        "PROT": [PROT],
        # Add more features here
    })

    prediction = model.predict(input_data)

    st.write("Prediction:")
    if prediction[0] == 0:
        st.write("No Hepatitis C (Class 0)")
    else:
        st.write("Hepatitis C (Class 1)")
