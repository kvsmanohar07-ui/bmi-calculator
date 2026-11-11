import streamlit as st

st.title("BMI Calculator")
st.write("Made by K.V.S. Manohar Reddy")

weight = st.number_input("Enter your weight in kg", min_value=1)
height = st.number_input("Enter your height in meters", min_value=0.1)

if st.button("Calculate BMI"):
    bmi = weight / (height * height)
    bmi = round(bmi, 2)
    st.success(f"Your BMI is {bmi}")

    if bmi < 18.5:
        st.write("Category: Underweight")
    elif bmi < 24.9:
        st.write("Category: Normal")
    elif bmi < 29.9:
        st.write("Category: Overweight")
    else:
        st.write("Category: Obese")
