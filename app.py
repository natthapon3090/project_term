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
