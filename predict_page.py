import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model
@st.cache_resource
def load_model():
    return joblib.load("final_rf_model.pkl")

model = load_model()

# UI
def show_predict_page():
    st.title("EV Network Classifier")

    st.write("### Please fill in the station details to predict the EV Network")

    # Dropdown for states
    states = [
        'Select a state',
        'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID',
        'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC',
        'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC',
        'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'
    ]
    state = st.selectbox("State", states)

    status_code = st.selectbox("Status Code", ['E', 'P', 'T'])
    access_time = st.selectbox("Access Time Category", ['24/7', 'Business Hours', 'Limited Hours', 'Unknown'])
    pricing = st.selectbox("Pricing Category", ['Free', 'Varies', 'Unknown'])

    latitude = st.number_input("Latitude", format="%.6f")
    longitude = st.number_input("Longitude", format="%.6f")
    level2 = st.number_input("EV Level 2 EVSE Num", min_value=0)
    dc_fast = st.number_input("EV DC Fast Num", min_value=0)

    chademo = st.number_input("CHADEMO", min_value=0)
    j1772 = st.number_input("J1772", min_value=0)
    j1772combo = st.number_input("J1772COMBO", min_value=0)
    tesla = st.number_input("TESLA", min_value=0)

    year = st.number_input("Year Confirmed", min_value=2000, max_value=2025)
    month = st.number_input("Month Confirmed", min_value=1, max_value=12)

    if st.button("Predict EV Network"):

        # Validation for states
        if state == 'Select a state':
            st.error("Please select a valid state before predicting.")
            return  # Prevent further code execution

        # Validation for lat/lon with US limits
        if not (24 <= latitude <= 49):
            st.warning("Latitude seems out of range for US-based stations (24 to 49).")
        if not (-125 <= longitude <= -66):
            st.warning("Longitude seems out of range for US-based stations (-125 to -66).")
        if latitude is None or longitude is None:
            st.error("Please enter valid latitude and longitude.")
            return

        # Show success message after all validations are passed
        st.success("Valid input detected! Now making prediction...")

        # Constructing input data
        input_data = pd.DataFrame([{
            'latitude': latitude,
            'longitude': longitude,
            'state': state,
            'status_code': status_code,
            'access_time_category': access_time,
            'pricing_category': pricing,
            'ev_level2_evse_num': level2,
            'ev_dc_fast_num': dc_fast,
            'CHADEMO': chademo,
            'J1772': j1772,
            'J1772COMBO': j1772combo,
            'TESLA': tesla,
            'year_confirmed': year,
            'month_confirmed': month
        }])

        st.write("Input Data for Prediction:", input_data)

        # Making prediction
        prediction = model.predict(input_data)[0]
        st.subheader(f"Predicted EV Network: **{prediction}**")
        # Debug: show prediction probabilities
        prediction_proba = model.predict_proba(input_data)
        st.write("Prediction Probabilities:", prediction_proba)

        st.success("Prediction completed successfully!")
        st.subheader(f"Predicted EV Network: **{prediction}**")
