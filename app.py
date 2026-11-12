import streamlit as st

st.title("⚖️ BMI Calculator")
st.write("Made by K.V.S. Manohar Reddy | 【entity-OASIS¦canonical_name=OASIS】 INFOBYTE - Task 2")

st.write("Enter your details:")

# Inputs
weight = st.number_input("Enter Weight (in kg):", min_value=0.0, value=0.0, step=0.1)
height_cm = st.number_input("Enter Height (in cm):", min_value=0.0, value=0.0, step=0.1)

if st.button("Calculate BMI"):
    # Validation
    if weight <= 0 or height_cm <= 0:
        st.error("Please enter valid Weight and Height!")
    else:
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)

        st.success(f"Your BMI is: {bmi:.2f}")

        # Category + Health Tip - 【entity-OASIS¦canonical_name=OASIS】 rule
        if bmi < 18.5:
            st.info("Category: Underweight")
            st.write("Tip: Eat healthy, protein-rich food and consult a doctor for a diet plan.")
        elif bmi < 25:
            st.success("Category: Normal Weight")
            st.write("Tip: Great! Maintain this with regular exercise and balanced diet.")
        elif bmi < 30:
            st.warning("Category: Overweight")
            st.write("Tip: Try daily walking, reduce junk food and sugary drinks.")
        else:
            st.error("Category: Obese")
            st.write("Tip: Please consult a doctor. Start with light exercise and healthy diet.")

        # Extra info
        st.write("---")
        st.write("BMI Chart:")
        st.write("Below 18.5 = Underweight")
        st.write("18.5 - 24.9 = Normal")
        st.write("25 - 29.9 = Overweight")
        st.write("30 and above = Obese")
