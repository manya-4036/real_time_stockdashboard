
import streamlit as st
import pandas as pd
import plotly.graph_objs as go 
import yfinance as yf
import datetime

st.set_page_config(layout="wide")
st.title("📈 Real-Time Stock Market Dashboard")

# Sidebar Inputs
st.sidebar.header("Stock Selector")
stock_symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., AAPL, MSFT, TSLA)", "AAPL")
start_date = st.sidebar.date_input("Start Date", datetime.date(2024, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.date.today())

@st.cache_data(ttl=300)
def get_data(symbol, start, end):
    try:
        data = yf.download(symbol, start=start, end=end)
        return data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()

# Fetch data
df = get_data(stock_symbol, start_date, end_date)

# Display data and charts
if df.empty:
    st.error("No data found for the selected stock symbol.")
else:
    st.subheader(f"{stock_symbol} Stock Data")
    st.dataframe(df.tail())

    st.subheader("📊 Stock Price Chart")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close Price'))
    fig.update_layout(title=f"{stock_symbol} Closing Price",
                      xaxis_title='Date',
                      yaxis_title='Price (USD)',
                      template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📌 Key Financial Indicators")
    st.metric("Latest Closing Price", f"${df['Close'].iloc[-1]:.2f}")
    st.metric("Opening Price", f"${df['Open'].iloc[-1]:.2f}")
    st.metric("Day High", f"${df['High'].iloc[-1]:.2f}")
    st.metric("Day Low", f"${df['Low'].iloc[-1]:.2f}")
    st.metric("Volume", f"{df['Volume'].iloc[-1]:,}")
