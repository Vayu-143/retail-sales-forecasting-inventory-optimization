import streamlit as st
import pandas as pd

st.title("📊 Retail Forecast & Inventory Dashboard")

# Load data
df = pd.read_csv("outputs/forecast_results.csv")

st.subheader("📈 Forecast vs Actual")
st.line_chart(df[["qty_sold", "predictions"]])

st.subheader("📋 Data Preview")
st.dataframe(df.tail())

# Inventory
inv = pd.read_csv("outputs/inventory_results.csv")
st.subheader("📦 Inventory Recommendation")
st.write(inv)