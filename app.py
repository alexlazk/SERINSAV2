import streamlit as st
import pandas as pd
import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

DB_DRIVER = os.getenv("DB_DRIVER")
DB_SERVER = os.getenv("DB_SERVER")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

@st.cache_data(show_spinner=False)
def get_connection():
    conn_str = (
        f"DRIVER={DB_DRIVER};"
        f"SERVER={DB_SERVER};"
        f"DATABASE={DB_DATABASE};"
        f"UID={DB_USER};"
        f"PWD={DB_PASSWORD}"
    )
    return pyodbc.connect(conn_str)

st.title("Simple KPIs Dashboard")

try:
    conn = get_connection()
    st.success("Connected to database")
except Exception as e:
    st.error(f"Database connection failed: {e}")
    st.stop()

# Example query - replace with real KPI queries
query = "SELECT TOP 5 * FROM sys.objects"

try:
    df = pd.read_sql(query, conn)
    st.dataframe(df)
except Exception as e:
    st.error(f"Failed to run sample query: {e}")
