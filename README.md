# Personal Fitness Tracker 🚀  

A Streamlit web application that predicts **calories burned** based on user input such as age, BMI, duration of exercise, heart rate, body temperature, and gender. The app uses a pre-trained **Random Forest model** to make predictions and provides comparative insights.

---

## 📌 **Features**
- 📊 **Calorie Prediction**: Enter personal details, and the app predicts the calories you burn.
- 🔍 **Comparison with Others**: See how your stats compare to a dataset of similar individuals.
- 📈 **Similar Results**: Find other users with similar calorie consumption patterns.
- ⚡ **Interactive UI**: Uses **Streamlit** for a seamless and user-friendly experience.

---

## 🚀 **Getting Started**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/user-shubham/fitness-tracker-app.git
```

### **2️⃣ Install Dependencies**
Make sure you have **Python 3.8+** installed. Then, run:
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the App**
```bash
streamlit run app.py
```
This will launch the web application in your browser.

---

## 🏗 **Project Structure**
```
📂 personal-fitness-tracker
│── 📜 app.py             # Main Streamlit application
│── 📜 rf_model.pkl       # Pre-trained Random Forest model
│── 📜 processed.csv      # Dataset for comparison
│── 📂 helper_functions   # Utility functions (e.g., animations, dividers)
│── 📜 requirements.txt   # Required dependencies
│── 📜 README.md          # Project documentation
```

---

## 🛠 **Technologies Used**
- 🐍 **Python**  
- 📊 **Pandas**  
- 📦 **Scikit-Learn**  
- 🔥 **Streamlit**  


---


