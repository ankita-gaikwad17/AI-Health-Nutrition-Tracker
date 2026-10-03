import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# 1. Train the Machine Learning Model directly inside the app
data = {
    'Calories': [500, 520, 90, 80, 450, 60, 480, 100],
    'Sugar': [45, 50, 5, 4, 35, 6, 40, 7],
    'Fiber': [1, 2, 6, 7, 2, 5, 1, 6],
    'Label': [0, 0, 1, 1, 0, 1, 0, 1]  # 0: Junk Food, 1: Healthy Food
}

df = pd.DataFrame(data)
X = df[['Calories', 'Sugar', 'Fiber']]
y = df['Label']

model = DecisionTreeClassifier()
model.fit(X, y)

# 2. Web App Interface
st.title("AI Health Nutrition Tracker")
st.write("Enter the food item's nutritional values below. Our trained Decision Tree AI model will predict whether it is Healthy or Junk Food:")

# Sliders for user inputs
calories = st.slider("Calories (kcal)", 50, 1000, 300)
sugar = st.slider("Sugar (g)", 0, 100, 10)
fiber = st.slider("Fiber (g)", 0, 50, 5)

# 3. Predict using the ML Model on button click
if st.button("Run AI Prediction"):
    # Pass input values into the machine learning model
    input_data = pd.DataFrame([[calories, sugar, fiber]], columns=['Calories', 'Sugar', 'Fiber'])
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.success("🎉 Prediction: This is Healthy Food! ✅")
    else:
        st.error("⚠️ Prediction: This is Junk Food! ❌")

st.markdown("---")
st.caption("Powered by Scikit-Learn Decision Tree Classifier | Built with Python & Streamlit")
