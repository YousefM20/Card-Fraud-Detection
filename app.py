import streamlit as st
import pandas as pd
import joblib
import random

# ============ Step 1: Load the trained model ============
model = joblib.load("fraud_detector_rf.pkl")

# ============ Step 2: Define features ============
selected_features = ['V1', 'V3', 'V5', 'V7', 'V10', 'V12', 'V14', 'V17', 'V20', 'Amount_Scaled']
all_features = [
    'V1','V2','V3','V4','V5','V6','V7','V8','V9',
    'V10','V11','V12','V13','V14','V15','V16','V17','V18','V19',
    'V20','V21','V22','V23','V24','V25','V26','V27','V28','Amount_Scaled'
]

# ============ Step 3: App Header ============
st.title("💳 Credit Card Fraud Detector")
st.write("Enter transaction details below or click **Autofill** to populate sample values.")

# ============ Step 4: Autofill logic ============
autofill = st.button("🔁 Autofill Example")

# ============ Step 5: Input form ============
user_input = {}
for feat in selected_features:
    if autofill:
        # Generate a sample random value
        default_val = round(random.uniform(-5, 5), 2)
        user_input[feat] = default_val
        st.number_input(label=feat, value=default_val, key=feat)
    else:
        user_input[feat] = st.number_input(label=feat, value=0.0, key=feat)

# Build the full feature vector expected by the model
default_full = {f: user_input.get(f, 0.0) for f in all_features}
input_df = pd.DataFrame([default_full])

# ============ Step 6: Prediction ============
if st.button("🚨 Predict Fraud?"):
    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]
    st.subheader("🧾 Prediction Result")
    st.write(f"**Prediction:** {'⚠️ FRAUD' if pred == 1 else '✅ Not Fraud'}")
    st.write(f"**Confidence (Fraud Probability):** {prob:.2f}")

# ============ Step 7: Display Input Data ============
st.write("---")
st.write("🔍 Your Input Data:")
st.dataframe(input_df)
