import streamlit as st

st.title("AI Health Nutrition Tracker")
st.write("Enter the food item's nutritional values below to check if it is healthy or junk food:")

# Inputs for Food Nutrition
calories = st.slider("Calories (kcal)", 50, 1000, 300)
sugar = st.slider("Sugar (g)", 0, 100, 10)
fiber = st.slider("Fiber (g)", 0, 50, 5)

if st.button("Check Nutrition"):
    if calories > 500 or sugar > 30:
        st.error("⚠️ Prediction: This item is classified as Junk Food.")
    else:
        st.success("🎉 Prediction: This item is a Healthy food choice!")

st.markdown("---")
st.caption("AI-Powered Nutrition Analysis Tool | Built with Python & Streamlit")