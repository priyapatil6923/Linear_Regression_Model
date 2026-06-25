import streamlit as st
import joblib

# load the saves model
model=joblib.load("linear_Regression_model.pkl")

#app title
st.title('student marks prediction')
st.title('prediction marks based on study hours')

#user input
study_hours = st.number_input('Enter the number of study hours:', min_value=0.0,max_value=50.0, value=1.0,step=0.5)

#predict button
if st.button("Predict"):
    prediction = model.predict([[study_hours]])

    predicted_marks = prediction.item()

    st.success(f"Predicted marks: {predicted_marks:.2f}")