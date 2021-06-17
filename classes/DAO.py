
class DAO:

    @staticmethod
    def _every_province_index(tx):
        result = tx.run(
            "MATCH(p: Provincia) < -[r1]-(t: Tweet) "
            "RETURN apoc.map.setKey(p, 'indice', avg(t.indice)) AS Provincia"
        )
        return [provincia["Provincia"] for provincia in result.data() if provincia["Provincia"]["name"] != "Desconocida"]

    @staticmethod
    def _every_province_stats(tx):
        def get_object(provincia):

            POS = provincia["sentimientos"].get(
                "POS") if provincia["sentimientos"].get("POS") else 0
            NEG = provincia["sentimientos"].get(
                "NEG") if provincia["sentimientos"].get("NEG") else 0
            NEU = provincia["sentimientos"].get(
                "NEU") if provincia["sentimientos"].get("NEU") else 0

            return {
                'name': provincia["name"],
                'POS': POS,
                'NEG': NEG,
                'NEU': NEU
            }

        result = tx.run(
            "MATCH(p: Provincia) <-[r1]-(t: Tweet)-[r2] -> (s: Sentimiento) "
            "WITH p, collect(s.name) as sentimientos "
            "RETURN apoc.map.setKey(p, 'sentimientos', apoc.coll.frequenciesAsMap(sentimientos)) AS Provincia"
        )

        return [get_object(provincia["Provincia"]) for provincia in result.data()]

    @staticmethod
    def _stats_by_province(tx, nom_provincia):
        result = tx.run(
            "MATCH(p: Provincia { name: $nom_provincia }) < -[r1]-(t: Tweet)-[r2] -> (s: Sentimiento) "
            "WITH p, collect(s.name) as sentimientos "
            "RETURN apoc.map.setKey(p, 'sentimientos', apoc.coll.frequenciesAsMap(sentimientos)) AS Provincia",
            nom_provincia=nom_provincia
        )
        return result.data()[0]["Provincia"]

    @staticmethod
    def _create_tweet(tx, provincia, user_name, text, indice, sentimiento):

        result = tx.run(
            "MATCH (p: Provincia {name: $provincia}) "
            "MATCH (s: Sentimiento {name: $sentimiento}) "
            "CREATE (p) <-[r1: PROVIENE]-(t: Tweet)-[r2: SIENTE]->(s) "
            "SET t.user_name = $user_name "
            "SET t.text = $text "
            "SET t.indice = $indice "
            "RETURN (t)",
            provincia=provincia,
            user_name=user_name,
            text=text,
            indice=indice,
            sentimiento=sentimiento
        )

        return result.single()[0]

    @staticmethod
    def _all_tweets(tx):
        result = tx.run("MATCH(t:Tweet) "
                        "RETURN(t)")
        return [tweet["t"] for tweet in result.data()]
