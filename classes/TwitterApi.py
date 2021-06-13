from tweepy import OAuthHandler, API, Stream

class TwitterApi:
    """
    Para instanciar esta clase, es necesario pasar las credenciales (diccionario)
    que contenga: apiKey, apiKeySecret, accessToken y accessTokenSecret 
    """
    def __init__(self, credentials):
        self.auth = OAuthHandler(credentials["apiKey"], credentials["apiSecretKey"])
        self.auth.set_access_token(credentials["accessToken"], credentials["accessTokenSecret"])

    def get_stream_listener(self, stream_listener):
        stream = Stream(auth=self.auth, listener=stream_listener)
        return stream

    def get_api(self):
        return API(self.auth)    