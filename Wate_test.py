import streamlit as st
import joblib
import numpy as np

# --- Page Config ---
st.set_page_config(
    page_title="Water Quality Predictor",
    layout="centered",
    page_icon="💧"
)

# --- Custom CSS ---
st.markdown("""
    <style>
        body {
            background-color: #e6f2ff;
        }
        .main {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1, h3 {
            color: #007acc;
            text-align: center;
        }
        .stButton > button {
            background-color: #007acc;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 0.5rem 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.markdown("<h1>💧 Water Quality Prediction</h1>", unsafe_allow_html=True)

# --- Load Model ---
model = joblib.load("random_forest_model.joblib")

# --- Input Section ---
st.markdown("<h3>🧪 Enter the water quality parameters:</h3>", unsafe_allow_html=True)

columns = [
    "ph", "Hardness", "Solids", "Chloramines", "Sulfate",
    "Conductivity", "Organic_carbon", "Trihalomethanes", "Turbidity"
]

user_inputs = []

# Use 3 columns per row for better UI
for i in range(0, len(columns), 3):
    col_group = columns[i:i+3]
    cols = st.columns(3)
    for j, col_name in enumerate(col_group):
        with cols[j]:
            st.markdown(f"<span style='color:red; font-weight:bold'>{col_name}</span>", unsafe_allow_html=True)
            val = st.number_input("", format="%.2f", key=col_name)
            user_inputs.append(val)

# --- Prediction Button ---
st.markdown("### 🔍 Prediction Result")
if st.button("Check Potability 💡"):
    input_array = np.array([user_inputs])
    prediction = model.predict(input_array)[0]

    if prediction == 1:
        st.success("✅ The water is *Potable* (Safe to drink).")
    else:
        st.error("🚫 The water is *Not Potable* (Unsafe to drink).")
