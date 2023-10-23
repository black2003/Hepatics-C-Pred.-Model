import streamlit as st
import pandas as pd
import joblib

# Load your trained model
model = joblib.load("Logistic Regression(1).pkl")

# Create a Streamlit web app
st.title("Hepatitis C Prediction")

st.write("Enter the required information to predict Hepatitis C.")

# User input
st.sidebar.header("User Input")
age = st.sidebar.slider("Age", 1, 100, 25)
sex = st.sidebar.radio("Sex", ("male", "female"))
# Add more input fields for other features as needed

# Feature preprocessing (ensure it's the same as in your training data)

# Predict
if st.button("Predict"):
    input_data = pd.DataFrame({
        "Age": [age],
        "Sex": [sex],
        # Add more features here
    })

    prediction = model.predict(input_data)

    st.write("Prediction:")
    if prediction[0] == 0:
        st.write("No Hepatitis C (Class 0)")
    else:
        st.write("Hepatitis C (Class 1)")
