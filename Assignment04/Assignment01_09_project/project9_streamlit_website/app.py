import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("My First Streamlit Website")

# Text input
name = st.text_input("Enter your name:")

# Button and greeting
if st.button("Greet me"):
    st.write(f"Hello, {name}! 👋")

# Create random data
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['A', 'B', 'C']
)

# Display line chart
st.line_chart(data)
