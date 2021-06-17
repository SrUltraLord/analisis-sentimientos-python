
from numpy import iinfo
import pandas as pd
import json

from classes.DBConn import DBConn
from classes.DAO import DAO

with open("settings.json") as json_file:
    settings = json.load(json_file)

db_conn = DBConn(settings["db"])
dao = DAO()

data = db_conn.get_every_province_stats(dao._every_province_stats)

print(data)

info = json.loads(json.dumps(data))

df = pd.json_normalize(info)

df.to_csv("prueba.csv")
