import streamlit as st
import joblib
import numpy as np

# load the saved regression model
model=joblib.load('regression_model.joblib')

# streamlit app ui title
st.title("Job Package Prediction Based on CGPA")
st.write("Enter your CGPA to predict the expected job package:")

# user input for cgpa
cgpa= st.number_input("CGPA",min_value=0.0,max_value=10.0,step=0.1)

# predict button
if st.button("Predict Package"):
    
    # prepare input data for model and predict the package
    prediction=model.predict(np.array([[cgpa]]))

    # convert numpy value to float
    predicted_value=float(prediction[0])

    # show the result
    st.success(f"Predicted Package: {predicted_value:,.2f} LPA")