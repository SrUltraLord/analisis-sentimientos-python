class DAO:

    @staticmethod
    def _create_tweet(tx, provincia, user_name, text, sentimiento):

        result = tx.run(
            "MATCH (p: Provincia {name: $provincia}) "
            "MATCH (s: Sentimiento {name: $sentimiento}) "
            "CREATE (p) <-[r1: PROVIENE]- (t: Tweet) -[r2: SIENTE]-> (s)"
            "SET t.user_name = $user_name "
            "SET t.text = $text "
            "RETURN (t)",
            provincia=provincia,
            user_name=user_name, 
            text=text,
            sentimiento=sentimiento
        )

        return result.single()[0]

    @staticmethod
    def _all_tweets(tx):
        result = tx.run("MATCH(t:Tweet) "
                        "RETURN(t)")
        return [tweet["t"] for tweet in result.data()] # if "declaraciones" in tweet["t"].get("text")]
