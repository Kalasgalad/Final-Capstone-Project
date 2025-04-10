import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import zipfile

@st.cache_data
def load_ev_data():
    # Loading the cleaned EV dataset
    df = pd.read_csv("clean_ev_data.csv")  # 
    return df

df = load_ev_data()

def show_explore_page():
    st.title("Explore EV Charging Station Data")
    st.write("### National Renewable Energy Lab - Alternative Fuel Stations")

    # 1. Number of stations by state
    st.write("#### Number of Stations by State")
    state_counts = df['state'].dropna().value_counts()
    st.bar_chart(state_counts)

    # 2. Number of stations by EV Network
    st.write("#### Number of Stations by EV Network")
    network_counts = df['ev_network_cleaned'].dropna().value_counts()
    st.bar_chart(network_counts)

    # 3. Average number of DC fast chargers per state
    st.write("#### Average DC Fast Chargers per State")
    avg_dc_fast = df.groupby("state")["ev_dc_fast_num"].mean().sort_values(ascending=False)
    st.bar_chart(avg_dc_fast)

    # 4. Station trends over time
    st.write("#### Station Confirmations Over Time")
    year_counts = df['year_confirmed'].value_counts().sort_index()
    st.line_chart(year_counts)

    # 5. Pie chart of pricing categories
    st.write("#### Pricing Category Distribution")
    pricing_data = df['pricing_category'].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(pricing_data, labels=pricing_data.index, autopct='%1.1f%%', startangle=90)
    ax1.axis("equal")
    st.pyplot(fig1)
