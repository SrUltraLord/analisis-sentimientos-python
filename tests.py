
arreglo = list(range(10))

for index, val in enumerate(arreglo):
    print(f"Indice: {index}, Valor: {val}")

# def secant(f, x1, x2, tol):
#     error = 1e3
#     n = 0
#     x3 = 0
#     while error > tol:
#         x3 = x1 - ((x2 - x1) / (f(x2) - f(x1))) * f(x1)
#         x1 = x2
#         x2 = x3
#         error = abs(f(x3))
#         n += 1
#     print("Approximate solution: {:.4f}".format(x3))
#     print("Number of iterations: {:d}".format(n))


# from numpy import iinfo
# import pandas as pd
# import json

# from classes.DBConn import DBConn
# from classes.DAO import DAO

# with open("settings.json") as json_file:
#     settings = json.load(json_file)

# db_conn = DBConn(settings["db"])
# dao = DAO()

# data = db_conn.get_every_province_stats(dao._every_province_stats)

# print(data)

# info = json.loads(json.dumps(data))

# df = pd.json_normalize(info)

# df.to_csv("prueba.csv")

# {'manabi', ',', 'ecuador'}
# {"quito", "cayambe", "machachi", "aloag", "sangolqui", "tabacundo"}
