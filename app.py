import streamlit as st

# App title
st.title("🚀 My First Streamlit App")

# Description
st.write("Welcome to my simple Streamlit application!")

# Sidebar
st.sidebar.title("User Input")

name = st.sidebar.text_input("Enter your name")

age = st.sidebar.number_input(
    "Enter your age",
    min_value=1,
    max_value=100,
    value=25
)

# Button
if st.button("Submit"):

    if name:
        st.success(f"Hello {name}! 👋")
        st.write(f"You are {age} years old.")

        # Simple logic
        if age >= 18:
            st.info("You are an adult.")
        else:
            st.warning("You are under 18.")

    else:
        st.error("Please enter your name.")