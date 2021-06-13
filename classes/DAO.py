class DAO:

    @staticmethod
    def _create_tweet(tx, user_name, text):
        result = tx.run("CREATE(t:Tweet) "
                        "SET t.user_name = $user_name "
                        "SET t.text = $text "
                        "RETURN 'Tweet Saved'", 
                        user_name=user_name, text=text)
        return result.single()[0]

    @staticmethod
    def _all_tweets(tx):
        result = tx.run("MATCH(t:Tweet) "
                        "RETURN(t)")
        return [tweet["t"] for tweet in result.data()] # if "declaraciones" in tweet["t"].get("text")]
