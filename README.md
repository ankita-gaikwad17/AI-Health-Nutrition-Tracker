AI Health Nutrition Tracker

A beginner-friendly machine learning project built with Python and Streamlit. It demonstrates how a Decision Tree classifier uses calories, sugar, and fiber values to predict sample healthy or junk food labels.

Features

- Interactive sliders for calories, sugar, and fiber.
- A Decision Tree Classifier for predictions.
- A simple Streamlit web interface.
- A Jupyter Notebook for exploring the model and its training.

Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Jupyter Notebook

How It Works

The model is trained on a small sample dataset containing calories, sugar, fiber, and example labels. Users can adjust the sliders and explore the model's predictions.

Limitations

This is an educational demonstration, not a medically validated nutrition tool. The model uses a small sample dataset, so its predictions should not be treated as reliable nutritional advice.

Run Locally

Install the required libraries:

pip install streamlit pandas scikit-learn

Start the app:

python -m streamlit run app.py
