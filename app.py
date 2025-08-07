import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Title of the App
st.title("Nifty Stocks Sector & Stock Explorer")

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("Nifty_Stocks.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Select Sector
sectors = df['Category'].unique()
selected_sector = st.selectbox("Select a Sector", sectors)

# Filter data for selected sector
sector_data = df[df['Category'] == selected_sector]

# Select Stock within the selected sector
stocks = sector_data['Symbol'].unique()
selected_stock = st.selectbox("Select a Stock", stocks)

# Filter data for selected stock
stock_data = sector_data[sector_data['Symbol'] == selected_stock]

# Plotting
st.subheader(f"{selected_stock} Closing Price Over Time")
plt.figure(figsize=(10, 5))
sb.lineplot(x=stock_data['Date'], y=stock_data['Close'])
plt.xticks(rotation=90)
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.title(f"{selected_stock} Stock Price Trend")
st.pyplot(plt)
