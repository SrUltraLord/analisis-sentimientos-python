import json
import tweepy

from classes.DAO import DAO
from textblob import TextBlob
from classes.DBConn import DBConn
from utils.functions import covert_to_tag
from classes.TwitterApi import TwitterApi
from textblob.sentiments import NaiveBayesAnalyzer
from utils.diccionario_provincias import diccionario
# from classes.Listener import StreamListener

if __name__ == '__main__':

    # Constantes
    NUM_OF_TWEETS = 10

    # Abrir el archivo de configuraciones y definirlo como diccionario
    # de Python
    with open("settings.json") as json_file:
        settings = json.load(json_file)

    # Creación del objeto para la API de twitter
    twitter_api = TwitterApi(settings["twitterCredentials"])

    # Solo es necesario si se va a hacer búsqueda de tweets en vivo
    # stream_listener = StreamListener()
    # stream = twitter_api.get_stream_listener(stream_listener)

    # Objeto para hacer la conexión con la Base de Datos
    db_conn = DBConn(settings["db"])
    # Objeto con las sentencias de Neo4J
    dao = DAO()

    # Se crea el objeto api que se obtiene del objeto twitter_api
    api = twitter_api.get_api()

    public_tweets = api.home_timeline()

    '''
    PARAMS DE BUSQUEDA DE LOS TWEETS
    '''
    query = "ecuador AND covid AND vacunacion"

    # Rectangulo de coordenadas. (Fucniona solo en streams)
    # Sup Izq: 1.625176, -91.698380
    # Inf Der: -4.868121, -75.195056
    # coords_ecuador = [-91.698380, -4.868121, -75.195056, 1.625176]

    # stream.filter(locations=coords_ecuador)

    tweet_list = tweepy.Cursor(
        api.search, q=query, lang="es").items(NUM_OF_TWEETS)

    for tweet in tweet_list:
        # Proceso de análisis de sentimientos.
        texto = TextBlob(tweet.text).translate(to='en')
        blob = TextBlob(str(texto), analyzer=NaiveBayesAnalyzer())
        sentimiento = covert_to_tag(blob.sentiment[1], blob.sentiment[2])

        # LOGS
        # print(f"@{tweet.user.screen_name}:\n{tweet.text}")
        # print(sentimiento)
        # print('*' * 60)

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
                sentimiento
            )
