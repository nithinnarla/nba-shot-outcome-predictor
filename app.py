import streamlit as st
import numpy as np

st.title("NBA Shot Outcome Predictor")
st.write("Enter shot details to predict outcome.")

# Input fields
x = st.number_input("X coordinate (feet)", min_value=-25.0, max_value=25.0, value=0.0)
y = st.number_input("Y coordinate (feet)", min_value=0.0, max_value=47.0, value=15.0)
shot_clock = st.slider("Shot clock remaining (seconds)", 0, 24, 12)
defenders = st.slider("Number of nearby defenders", 0, 5, 1)
dribbles = st.slider("Number of dribbles before shot", 0, 10, 1)

# Simple heuristic calculations
distance = np.sqrt(x**2 + y**2)
prob_3 = np.clip((distance - 16) / 12, 0.0, 1.0)
prob_2 = 1.0 - prob_3
prob_and_one = np.clip(0.05 + 0.05 * defenders, 0.05, 0.5)

# Normalize probabilities
total = prob_2 + prob_3 + prob_and_one
prob_2 /= total
prob_3 /= total
prob_and_one /= total

# Prediction logic
if st.button("Predict"):
    st.write(f"Probabilities:\n- 2-pointer: {prob_2:.2f}\n- 3-pointer: {prob_3:.2f}\n- and-one: {prob_and_one:.2f}")
    outcome = np.random.choice(['2-pointer', '3-pointer', 'and-one'], p=[prob_2, prob_3, prob_and_one])
    st.success(f"Predicted outcome: {outcome}")
