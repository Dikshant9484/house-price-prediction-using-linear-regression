import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 4, 2, 5, 6])

# Train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Streamlit app UI
st.title("Simple Linear Regression Predictor")

# Input from user
user_input = st.number_input("Enter a value for X to predict y:", value=1)

# Predict when button clicked
if st.button("Predict"):
    input_array = np.array([[user_input]])
    prediction = model.predict(input_array)
    st.write(f"Predicted value of y: {prediction[0]:.2f}")

# Show model parameters (optional)
st.write(f"Model coefficient (slope): {model.coef_[0]:.2f}")
st.write(f"Model intercept: {model.intercept_:.2f}")
