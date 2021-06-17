import numpy as np
import pandas as pd
import plotly.express as px
import json


def plot_mapbox():
    # Abrir el archivo JSON en modo de lectura
    with open('utils/map/gadm36_ECU_1.json', 'r') as myfile:
        data = myfile.read()

    geo_json = json.loads(data)
    df = pd.read_csv("stats_map.csv")

    fig = px.choropleth_mapbox(df,
                               geojson=geo_json,
                               color="indice",
                               locations="name",
                               featureidkey="properties.NAME_1",
                               center={
                                   "lat": -1.5,
                                   "lon": -80.7073
                               },
                               mapbox_style="carto-positron",
                               zoom=5.6,
                               opacity=.7,)

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    fig.show()


def plot_bars():
    wide_df = pd.read_csv("bar_graph.csv")
    fig = px.bar(wide_df, x="name", y=[
                 "POS", "NEG", "NEU"], title="Análisis de sentimientos por Provincia")

    fig.show()
