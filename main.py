import json
import tweepy
import pandas as pd

from classes.DAO import DAO
from textblob import TextBlob
from utils.graphs import plot_bars, plot_mapbox
from classes.DBConn import DBConn
from utils.functions import covert_to_tag, create_bar_plot_csv_from_neo4j, create_map_plot_csv_from_neo4j
from classes.TwitterApi import TwitterApi
from textblob.sentiments import NaiveBayesAnalyzer
from utils.diccionario_provincias import diccionario


if __name__ == '__main__':

    # Constantes
    NUM_OF_TWEETS = 5

    # Abrir el archivo de configuraciones y definirlo como diccionario
    # de Python
    with open("settings.json") as json_file:
        settings = json.load(json_file)

    # Creación del objeto para la API de twitter
    twitter_api = TwitterApi(settings["twitterCredentials"])

    # Objeto para hacer la conexión con la Base de Datos
    db_conn = DBConn(settings["db"])

    # Objeto con las sentencias de Neo4J
    dao = DAO()

    # Se crea el objeto api que se obtiene del objeto twitter_api
    api = twitter_api.get_api()

    '''
    PARAMS DE BUSQUEDA DE LOS TWEETS
    '''
    query = "(clases OR presenciales) AND retorno AND ecuador"

    '''
    BUSQUEDA DE LOS TWEETS Y GUARDAR EN LA BASE DE DATOS    
    '''
    tweet_list = tweepy.Cursor(
        api.search, q=query, lang="es").items(NUM_OF_TWEETS)

    for tweet in tweet_list:
        # Proceso de análisis de sentimientos.
        texto = TextBlob(tweet.text).translate(to='en')
        blob = TextBlob(str(texto), analyzer=NaiveBayesAnalyzer())
        tweet_index = blob.sentiment[1] - blob.sentiment[2]

        sentimiento = covert_to_tag(blob.sentiment[1], blob.sentiment[2])

        # La ubicación del tweet (en caso de que esté disponible)
        # se pasa a minúsculas y se quita las comaas y es transformada
        # en arreglo.
        location_arr = tweet.user.location.lower().replace(
            ",", " ").replace(".", " ").split()

        tweet_set = set(location_arr)

        for provincia in diccionario:
            # Intersección entre el set de ubicación del tweet
            # y el diccionario de sets por provincia.
            if diccionario[provincia].intersection(tweet_set):
                print(f"Encontrado en: {provincia}")
                db_conn.get_create_tweet_result(
                    dao._create_tweet,
                    provincia,
                    tweet.user.screen_name,
                    tweet.text,
                    tweet_index,
                    sentimiento
                )
                break
        else:
            # En caso de que no se encuentre provincia, llega hasta este punto
            print("Desconocida")
            db_conn.get_create_tweet_result(
                dao._create_tweet,
                "Desconocida",
                tweet.user.screen_name,
                tweet.text,
                tweet_index,
                sentimiento
            )
    '''
    CREACION DE LOS GRAFICOS
    '''
    # Grafico de Barras
    # Conversion de json (db) a csv
    # data = db_conn.get_every_province_stats(dao._every_province_stats)
    # create_bar_plot_csv_from_neo4j(data)

    # plot_bars()

    # Grafico de Mapa
    # data_map = db_conn.get_every_province_index(dao._every_province_index)
    # create_map_plot_csv_from_neo4j(data_map)

    # plot_mapbox()
