import json
import tweepy

from classes.DAO import DAO
from classes.DBConn import DBConn
from classes.TwitterApi import TwitterApi
from classes.Listener import StreamListener

if __name__ == '__main__':  
    
    # Abrir el archivo de configuraciones y definirlo como diccionario
    # de Python
    with open("settings.json") as json_file:
        settings = json.load(json_file)

    twitterApi = TwitterApi(settings["twitterCredentials"])
    # stream_listener = StreamListener()

    db_conn = DBConn(settings["db"])
    dao = DAO()
    # DANN MECO
    def danngei():
        print("DANN MECO")
        
    api = twitterApi.get_api()
    # stream = twitterApi.get_stream_listener(stream_listener)


    public_tweets = api.home_timeline()

    # db_conn.get_all_tweets_result(dao._all_tweets)
    # db_conn.get_create_person_result(dao._create_person, "Persona1", "xd")
    # db_conn.get_all_tweets_result(dao._all_tweets)

    '''
    PARAMS DE BUSQUEDA DE LOS TWEETS
    '''
    # query = "michis OR michi OR gato OR gatos"
    # query = "ecuador AND covid AND vacunacion"
    query = "ecuador"
    ecuador = [-80.999585,-5.023681,-75.186973,1.338060]

    tweet_list = tweepy.Cursor(api.search, q=query, lang="es", ).items(100)

    diccionario_provincias = {
        "Pichincha": ["quito"]
    }

    for tweet in tweet_list:
        try:
            str_location = tweet.user.location.lower()
            print(str_location if str_location != "" else "No hay ubicación")
            # if "quito" in tweet.user.location.lower():
                # print("es quiteño")
        except Exception:
            print("La tonta no puso location")
        # db_conn.get_create_tweet_result(dao._create_tweet, tweet.user.screen_name, tweet.text)
        # print(f"@{tweet.user.screen_name}:\n{tweet.text}")
        # print('*' * 60)

    # greeter = App(uri=URI, user=DB_USER, password=DB_PASS)
    # greeter.get_create_person_result("Pato", "Estudiante")
    # greeter.close()

