
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Aspirin Decision Support", layout="centered")
st.title("ðŸš‘ Aspirin Recommendation Model")

st.markdown("""
This is a prototype to support emergency decisions for giving aspirin to patients over 50 years old.
**Note:** This tool is for demonstration purposes only and does not replace medical judgment.
""")

# Input fields
age = st.number_input("Patient Age", min_value=0, max_value=120, value=40)
chest_pain = st.selectbox("Does the patient have chest pain?", ["No", "Yes"])
bp = st.number_input("Systolic Blood Pressure", min_value=0, max_value=300, value=120)
heart_rate = st.number_input("Heart Rate", min_value=0, max_value=250, value=80)

submit = st.button("Run Recommendation")
recommendation = ""

if submit:
    if age >= 50 and chest_pain == "Yes":
        recommendation = "âœ… Recommendation: Give aspirin 300mg. Probability of benefit is high (above 90%)."
        st.success(recommendation)
    elif age >= 50:
        recommendation = "â„¹ï¸ Caution: Patient is above 50. Consider other factors before prescribing aspirin."
        st.info(recommendation)
    else:
        recommendation = "âŒ Recommendation: Aspirin not recommended based on current inputs."
        st.warning(recommendation)

    # Add outcome recording
    outcome = st.selectbox("Did the patient improve after aspirin?", ["Unknown", "Yes", "No"])

    # Save to CSV
    record = {
        "Age": age,
        "Chest_Pain": chest_pain,
        "BP": bp,
        "HR": heart_rate,
        "Recommendation": recommendation,
        "Outcome": outcome
    }

    df = pd.DataFrame([record])
    file_path = "aspirin_records.csv"

    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', index=False, header=False)
    else:
        df.to_csv(file_path, index=False)

    st.success("âœ… Patient record saved.")
