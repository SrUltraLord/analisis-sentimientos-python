import json
import pandas as pd


def covert_to_tag(positivo, negativo):
    if (.45 < positivo < .55) and (.45 < negativo < .55):
        return "NEU"
    if positivo > .55:
        return "POS"
    if negativo > .55:
        return "NEG"

    return "UNK"


def create_bar_plot_csv_from_neo4j(data):
    info = json.loads(json.dumps(data))
    df = pd.json_normalize(info)
    df.to_csv("bar_graph.csv")


def create_map_plot_csv_from_neo4j(data):
    info = json.loads(json.dumps(data))
    df = pd.json_normalize(info)
    df.to_csv("stats_map.csv")
