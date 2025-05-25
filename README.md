first make an enviiornment for the code to run using python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows
in the terminal.

now Install Required Libraries
Run this in your terminal to install all necessary Python packages:
bash
Copy
Edit
pip install streamlit pandas plotly yfinance.
Run the Streamlit App

Once dependencies are installed and you're in the same directory as stock_dashboard.py, run:
bash
Copy
Edit
streamlit run stock_dashboard.py

What Happens Next
A browser window will open automatically at http://localhost:8501/.

You can enter stock symbols like AAPL, GOOGL, MSFT, etc.

You'll see a line chart, latest prices, and financial metrics updated live.
