from neo4j import GraphDatabase
from pprint import pprint


class DBConn:
    """
    Para el constructor de esta clase es necesario pasarle el objeto
    db_config con los atributos: host, port, user y pass.
    """

    def __init__(self, db_config):
        self.uri = f"bolt://{db_config['host']}:{db_config['port']}"
        self.driver = GraphDatabase.driver(
            self.uri, auth=(db_config["user"], db_config["pass"]))
        self.session = self.driver.session(database=db_config["database"])

    # Funcion para cerrar el driver.
    def close(self):
        self.driver.close()

    """
    Funciones para obtener los resultados de DAO.
    """

    def get_every_province_index(self, _every_province_index):
        with self.session as session:
            result = session.write_transaction(_every_province_index)
            return result

    def get_every_province_stats(self, _every_province_stats):
        with self.session as session:
            result = session.write_transaction(_every_province_stats)
            return result

    def get_stats_by_province(self, _stats_by_province, nom_provincia):
        with self.session as session:
            result = session.write_transaction(
                _stats_by_province, nom_provincia)
            pprint(result)

    def get_create_tweet_result(self, _create_tweet, provincia, user_name, text, indice, sentimiento):
        with self.session as session:
            result = session.write_transaction(
                _create_tweet, provincia, user_name, text, indice, sentimiento)
            # print(result)

    def get_all_tweets_result(self, _all_tweets):
        with self.session as session:
            result = session.write_transaction(_all_tweets)
            pprint.pprint(result)
