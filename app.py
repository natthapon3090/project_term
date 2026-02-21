import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pycaret.classification import load_model, predict_model

# โหลดข้อมูลดิบ
with open("dataset.csv", "r", encoding="utf-8") as f:
    first_line = f.readline()

if ";" in first_line:
    df_raw = pd.read_csv("dataset.csv", sep=";", engine="python")
else:
    df_raw = pd.read_csv("dataset.csv", engine="python")

model = load_model("model_programming")

app = dash.Dash(__name__)

# ---------- Slider block ----------
def slider_block(label, id_name, min_v, max_v, default):
    return html.Div([
        html.Label(label, style={"fontWeight":"bold","fontSize":"18px"}),

        html.Div(id=f"{id_name}_value",
                 style={
                     "fontSize":"22px",
                     "color":"#ffd700",
                     "marginBottom":"5px"
                 }),

        dcc.Slider(
            min=min_v,
            max=max_v,
            step=1,
            value=default,
            id=id_name,
            marks={i: str(i) for i in range(min_v, max_v+1)},
            tooltip={"placement": "bottom", "always_visible": True}
        ),
        html.Br()
    ])
