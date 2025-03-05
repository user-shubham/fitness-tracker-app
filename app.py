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


# Get user input
display_data, prediction_data = get_user_input()

# Display user parameters
section_divider()
st.header("Your Parameters")
loading_animation()
st.write(display_data)

# Predict calorie consumption
predicted_calories = calorie_prediction_model.predict(prediction_data)

# Display prediction
section_divider()
st.header("Prediction:")
loading_animation()
st.write(f"{round(predicted_calories[0], 2)} **kilocalories**")

# Load processed dataset
section_divider()
st.header("Similar Results")
dataset = pd.read_csv('processed.csv')
loading_animation()

# Filter dataset to find similar calorie consumption records
calorie_range = (predicted_calories[0] - 10, predicted_calories[0] + 10)
similar_entries = dataset.query("`Calorie Consumption` >= @calorie_range[0] and `Calorie Consumption` <= @calorie_range[1]")

# Ensure at most 5 entries are displayed
st.write(similar_entries.head(5))

# Calculate percentile comparisons efficiently
st.write(f"You are older than {dataset['Age'].lt(display_data['Age'].values[0]).mean() * 100:.2f}% of other people.")
st.write(f"Your exercise duration is higher than {dataset['Duration'].lt(display_data['Duration'].values[0]).mean() * 100:.2f}% of other people.")
st.write(f"You have a higher heart rate than {dataset['Heart Rate'].lt(display_data['Heart Rate'].values[0]).mean() * 100:.2f}% of other people during exercise.")
st.write(f"You have a higher body temperature than {dataset['Body Temperature'].lt(display_data['Body Temperature'].values[0]).mean() * 100:.2f}% of other people during exercise.")
