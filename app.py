from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# โหลด CSV จาก Kaggle
df = pd.read_csv("nvidia_stock.csv")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna()

app = Dash(__name__)
app.title = "NVIDIA Dashboard"

app.layout = html.Div([

    html.H1("📈 NVIDIA Stock Dashboard", style={"textAlign": "center"}),

    html.Div([
        dcc.DatePickerRange(
            id="date-picker",
            start_date=df["Date"].min(),
            end_date=df["Date"].max()
        ),

        dcc.Dropdown(
            id="ma-dropdown",
            options=[
                {"label": "MA 20", "value": 20},
                {"label": "MA 50", "value": 50},
                {"label": "MA 100", "value": 100}
            ],
            value=20
        )
    ], style={"width": "60%", "margin": "auto"}),

    dcc.Graph(id="price-chart"),
    dcc.Graph(id="volume-chart"),
    dcc.Graph(id="ma-chart")

])
