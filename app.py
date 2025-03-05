import streamlit as st
import pandas as pd
import pickle
import warnings
from helper_functions import section_divider, loading_animation

# Suppress warnings
warnings.filterwarnings('ignore')

# App Title and Description
st.write('## Personal Fitness Tracker')
st.write('This WebApp predicts the number of calories burned based on your personal parameters such as `Age`, `Gender`, `BMI`, etc.')

# Load the trained model
with open('rf_model.pkl', 'rb') as model_file:
    calorie_prediction_model = pickle.load(model_file)

st.sidebar.header('Enter Your Details')

def get_user_input():
    """Collects user input and returns formatted DataFrames for display and prediction."""
    # Sidebar input widgets
    age = st.sidebar.slider("Age:", 10, 100, 30)
    bmi = st.sidebar.slider("BMI:", 15, 40, 20)
    duration = st.sidebar.slider("Exercise Duration (min):", 0, 35, 15)
    heart_rate = st.sidebar.slider("Heart Rate (bpm):", 60, 130, 80)
    body_temperature = st.sidebar.slider("Body Temperature (°C):", 36, 42, 38)
    gender = st.sidebar.radio("Gender:", ("Male", "Female"))

    # Convert gender to numeric (1 for Male, 0 for Female)
    gender_numeric = 1 if gender == "Male" else 0

    # Create DataFrame for display
    user_input_df = pd.DataFrame({
        "Age": [age],
        "BMI": [bmi],
        "Duration": [duration],
        "Heart Rate": [heart_rate],
        "Body Temperature": [body_temperature],
        "Gender": [gender]
    })

    # Create DataFrame for model input
    model_input_df = pd.DataFrame({
        "Age": [age],
        "BMI": [bmi],
        "Duration": [duration],
        "Heart Rate": [heart_rate],
        "Body Temperature": [body_temperature],
        "Gender_male": [gender_numeric]
    })

    return user_input_df, model_input_df
