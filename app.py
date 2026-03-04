import streamlit as st
import joblib
import pandas as pd

# ---------- Page Config ----------
st.set_page_config(
    page_title="Vehicle Service Cost Predictor",
    page_icon="🚗",
    layout="wide"
)

# ---------- Load Artifacts ----------
model = joblib.load("Servicecostmodel.pkl")
preprocessor = joblib.load("preprocessor.pkl")

# ---------- Title ----------
st.title("🚗 Vehicle Service Cost Predictor")
st.markdown("Predict the estimated vehicle service cost using ML")

# ---------- Sidebar Inputs ----------
st.sidebar.header("🔧 Enter Vehicle Details")

vehicle_age = st.sidebar.number_input(
    "Vehicle Age (years)",
    min_value=0,
    value=3
)

warranty_flag = st.sidebar.selectbox(
    "Warranty Status",
    [0, 1],
    format_func=lambda x: "Under Warranty" if x == 1 else "No Warranty"
)

base_price = st.sidebar.number_input(
    "Base Price",
    min_value=0,
    value=500000
)

service_type = st.sidebar.selectbox(
    "Service Type",
    ["Minor", "Major", "Repair"]
)

engine_type = st.sidebar.selectbox(
    "Engine Type",
    ["Petrol", "Diesel", "Electric"]
)

segment = st.sidebar.selectbox(
    "Segment",
    ["SUV", "Sedan", "Hatchback","Electric"]
)

dealer_region = st.sidebar.selectbox(
    "Dealer Region",
    ["Chennai", "Mumbai", "Delhi", "Bangalore", "Hyderabad"]
)

# ---------- Predict Button ----------
predict_btn = st.sidebar.button("🚀 Predict Cost")

# ---------- Main Layout ----------
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📋 Input Summary")

    input_df = pd.DataFrame({
        "VEHICLE_AGE": [vehicle_age],
        "WARRANTY_FLAG": [warranty_flag],
        "BASE_PRICE": [base_price],
        "SERVICE_TYPE": [service_type],
        "ENGINE_TYPE": [engine_type],
        "SEGMENT": [segment],
        "DEALER_REGION": [dealer_region],
    })

    st.dataframe(input_df, use_container_width=True)

with col2:
    st.subheader("💰 Prediction")

    if predict_btn:
        processed = preprocessor.transform(input_df)
        prediction = model.predict(processed)[0]

        st.success(f"Estimated Service Cost: ₹ {prediction:,.2f}")

        st.metric(
            label="Predicted Cost",
            value=f"₹ {prediction:,.0f}"
        )
    else:
        st.info("Enter details in the sidebar and click Predict")

# ---------- Footer ----------
st.markdown("---")
st.caption("Built with Streamlit • ML Project")

