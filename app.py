from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# ===============================
# LOAD DATA
# ===============================

df = pd.read_csv("nvidia_stock.csv")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna()

# ===============================
# APP SETUP (Dark Theme)
# ===============================

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = "NVIDIA Advanced Dashboard"

# ===============================
# KPI CALCULATION
# ===============================

latest_close = df["Close"].iloc[-1]
previous_close = df["Close"].iloc[-2]
change_percent = ((latest_close - previous_close) / previous_close) * 100
latest_volume = df["Volume"].iloc[-1]
