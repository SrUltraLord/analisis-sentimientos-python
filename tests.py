
nums = [1, 2, 3]

nums_2 = map(lambda x: x**2, nums)
print(list(nums_2))

# from textblob import TextBlob
# from textblob.sentiments import NaiveBayesAnalyzer

# oracionesxd = [
#     "El wesos es malito.",
#     "Patricio es muy buen amigo.",
#     "Humitas de sal o de dulce?",
#     ]

# for oracion in oracionesxd:
#     texto = TextBlob(oracion).translate(to='en')
#     print(texto)
#     blob = TextBlob(str(texto), analyzer=NaiveBayesAnalyzer())
#     print(blob.sentiment[0], blob.sentiment[1], blob.sentiment[2])
#     # print(blob.pos_tagger)

#                 # 0 a 1     0 a 1
# def covert_to_tag(positivo, negativo):

#     tag = "UNK"

#     if (.45 < positivo < .55) and (.45 < negativo < .55):
#         tag = "NEU"
#         return tag

#     if positivo > .55:
#         tag = "POS"
#         return tag

#     tag = "NEG"
#     return tag


# from translate import Translator

# oracionesxd = [
#     "El wesos es malito.",
#     "Patricio es muy buen amigo.",
#     "Daniel hijo de puta.",
#     "Humitas de sal o de dulce?",
#     "Daniel perra tonta"
#     ]

# translator = Translator(to_lang="en")

# for oracion in oracionesxd:
#     translation = translator.translate(oracion)
#     print(translation)

# import twitterSentiment

# oraciones = [
#     # "El wesos es malito.",
#     # "Patricio es muy buen amigo.",
#     # "Daniel hijo de puta.",
#     # "Humitas de sal o de dulce?",
#     # "Daniel perra tonta"
#     "My friend Pato is a nice guy",
#     "Randely is great!",
#     "Daniel Arias is a good friend",
#     "Jordy is a bad person"
#     ]

# query = "ecuador AND covid"

# connection = twitterSentiment.API()

# search = connection.querySearch(query, count=1, result_type='recent', lang='es')
# data = twitterSentiment.StructureStatusesData(search)
# sentiment = twitterSentiment.SentimentScore(data.getTweet())
# print(sentiment.getSentimentClassification())

# def get_feeling(text):
#     search = connection.querySearch(text, count=1, result_type='recent', lang='en')
#     data = twitterSentiment.StructureStatusesData(search)
#     sentiment = twitterSentiment.SentimentScore(data.getTweet())
#     print(sentiment.getSentimentClassification())

# for tweet in oraciones:
#     print(tweet)
#     get_feeling(tweet)

# ==========================================================

# import meaningcloud as mc

# LICENSE_KEY = '5fb989721f3ea1e5bb6f3940b5a42949'

# oraciones = [
#     "El wesos es malito.",
#     "Patricio es muy buen amigo.",
#     "Daniel hijo de puta.",
#     "Humitas de sal o de dulce?",
#     "Daniel perra tonta"
#     ]

# def get_feeling(tweet):
#     sentiment_req = mc.SentimentRequest(LICENSE_KEY, lang='es', txt=tweet, txtf='markup').sendReq()
#     sentiment_res = mc.SentimentResponse(sentiment_req)

#     if sentiment_res.isSuccessful() is False:
#         return "0"

#     return sentiment_res.getGlobalScoreTag()

# for tweet in oraciones:
#     print(tweet)
#     print(get_feeling(tweet))

# ==========================================================

# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# oraciones = [
#     "El wesos es malito.",
#     "Patricio es muy buen amigo.",
#     "Daniel hijo de puta.",
#     "Humitas de sal o de dulce?",
#     "Daniel perra tonta"
#     ]

# oraciones_open_english = [
#     "My friend Pato is a nice guy",
#     "Randely is great!",
#     "Daniel Arias is a good friend",
#     "Jordy is a bad person"
# ]

# analyzer = SentimentIntensityAnalyzer()

# for oracion in oraciones_open_english:
#     valores = analyzer.polarity_scores(oracion)
#     print(valores["compound"])


# ==========================================================
# Demora mucho y no es muy preciso :c

# from sentiment_analysis_spanish import sentiment_analysis

# oraciones = [
#     "El wesos es malito.",
#     "Patricio es muy buen amigo.",
#     "Daniel hijo de puta.",
#     "Humitas de sal o de dulce?",
#     "Daniel perra tonta"
#     ]

# sentiment = sentiment_analysis.SentimentAnalysisSpanish()
# for oracion in oraciones:
#     print(oracion)
#     print(sentiment.sentiment(oracion))

# ==========================================================

# import nltk

# from nltk import sentiment, word_tokenize
# from nltk.tokenize import ToktokTokenizer
# from nltk.sentiment.vader import SentimentIntensityAnalyzer

# tokenizer = nltk.data.load("tokenizers/punkt/spanish.pickle")
# # sentences = tokenizer.tokenize("El wesos es malito. Patricio es muy buen amigo. Daniel hijo de puta. Humitas de sal o de dulce?")
# sentences = tokenizer.tokenize("I like bread. My friend is dumb af. Daniel sucks dicks. Dangely is such a great friend!")
# # toktok = ToktokTokenizer()
# # sentences = toktok.tokenize("El wesos es malito. Patricio es muy buen amigo. Daniel hijo de puta. Humitas de sal o de dulce?")

# analizador = SentimentIntensityAnalyzer()

# for sentence in sentences:
#     print(sentence)
#     scores = analizador.polarity_scores(sentence)
#     for key in scores:
#         print(key, ': ', scores[key])
#         print()

# ==========================================================
