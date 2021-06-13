from neo4j import GraphDatabase
import pprint

class DBConn:
    """
    Para el constructor de esta clase es necesario pasarle el objeto
    db_config con los atributos: host, port, user y pass.
    """
    def __init__(self, db_config):
        self.uri = f"bolt://{db_config['host']}:{db_config['port']}"
        self.driver = GraphDatabase.driver(self.uri, auth=(db_config["user"], db_config["pass"]))
        self.session = self.driver.session(database=db_config["database"])

    # Funcion para cerrar el driver.
    def close(self):
        self.driver.close()

    """
    Funciones para obtener los resultados de DAO.
    """

    def get_create_tweet_result(self, _create_tweet, user_name, text):
        with self.session as session:
            result = session.write_transaction(_create_tweet, user_name, text)
            print(result)

    def get_all_tweets_result(self, _all_tweets):
        with self.session as session:
            result = session.write_transaction(_all_tweets)
            pprint.pprint(result)
