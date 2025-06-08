
import streamlit as st

st.set_page_config(page_title="Aspirin Decision Support", layout="centered")
st.title("🚑 Aspirin Recommendation Model")

st.markdown("""
This is a simple prototype to support emergency decisions for giving aspirin to patients over 50 years old.
**Note:** This tool is for demonstration purposes only and does not replace medical judgment.
""")

# Input fields
age = st.number_input("Patient Age", min_value=0, max_value=120, value=40)
chest_pain = st.selectbox("Does the patient have chest pain?", ["No", "Yes"])

bp = st.number_input("Systolic Blood Pressure", min_value=0, max_value=300, value=120)
heart_rate = st.number_input("Heart Rate", min_value=0, max_value=250, value=80)

submit = st.button("Run Recommendation")

# Logic for simple model (mock example)
if submit:
    if age >= 50 and chest_pain == "Yes":
        st.success("✅ Recommendation: Give aspirin 300mg. Probability of benefit is high (above 90%).")
    elif age >= 50:
        st.info("ℹ️ Caution: Patient is above 50. Consider other factors before prescribing aspirin.")
    else:
        st.warning("❌ Recommendation: Aspirin not recommended based on current inputs.")
