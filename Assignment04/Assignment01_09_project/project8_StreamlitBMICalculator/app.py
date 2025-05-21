# app.py

import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height ** 2)

st.title("BMI Calculator")

# Input fields
weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (meters)", min_value=0.1, step=0.01)

# Button to calculate BMI
if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    st.success(f"Your BMI is {bmi:.2f}")
    
    # BMI Category
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.info("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
