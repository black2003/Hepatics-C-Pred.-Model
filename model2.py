import streamlit as st
import pandas as pd
import joblib
import altair as alt

# Load your trained model
model = joblib.load(r"C:\Users\asus\Downloads\PDS\Logistic Regression.pkl")

# Set page title and favicon
st.set_page_config(page_title="Hepatitis C Prediction", page_icon=":microbe:")

# Create a Streamlit web app
st.title("Hepatitis C Prediction")
st.write("Enter the required information to predict Hepatitis C.")

# User input
st.sidebar.header("User Input")
age = st.sidebar.slider("Age", 1, 100, 25)
sex = st.sidebar.radio("Sex", (0, 1))
ALB = st.sidebar.slider("ALB", 1, 100, 25)
ALP = st.sidebar.slider("ALP", 1, 100, 25)
ALT = st.sidebar.slider("ALT", 1, 100, 25)
AST = st.sidebar.slider("AST", 1, 200, 25)
BIL = st.sidebar.slider("BIL", 1, 100, 25)
CHE = st.sidebar.slider("CHE", 1, 100, 25)
CHOL = st.sidebar.slider("CHOL", 1, 100, 25)
CREA = st.sidebar.slider("CREA", 1, 100, 25)
GGT = st.sidebar.slider("GGT", 1, 100, 25)
PROT = st.sidebar.slider("PROT", 1, 100, 25)
# Add more input fields for other features as needed

# Feature preprocessing (ensure it's the same as in your training data)

# Add a little space for aesthetics
st.write("")

# Predict
if st.button("Predict"):
    # Create a DataFrame with feature names that match your model
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

    # Modify this line to match the feature names used during training
    prediction_proba = model.predict_proba(input_data)

    st.write("### Prediction Probability:")
    st.write(f"Probability of No Hepatitis C (Class 0): {prediction_proba[0][0]:.2f}")
    st.write(f"Probability of Hepatitis C (Class 1): {prediction_proba[0][1]:.2f}")


    # Create a simple example chart using Altair (you can replace this with your data)
    chart_data = pd.DataFrame({"Category": ["No Hepatitis C", "Hepatitis C"], "Probability": [prediction_proba[0][0], prediction_proba[0][1]]})
    chart = alt.Chart(chart_data).mark_bar().encode(x="Category", y="Probability")
    st.altair_chart(chart, use_container_width=True)
