from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analysis = TextBlob("TextBlob sure looks like it has some interesting features!")

print(dir(analysis.sentiment))