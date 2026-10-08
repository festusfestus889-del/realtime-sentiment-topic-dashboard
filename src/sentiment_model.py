import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
os.makedirs("data/processed", exist_ok=True)

df = pd.read_csv("data/raw/stream.csv")
analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
  score = analyzer.polarity_scores(text)['compound']
  if score >= 0.05: return "positive", score
  elif score <= -0.05: return "negative", score
  else: return "neutral", score

df[['sentiment','sentiment_score']] = df['text'].apply(lambda x: pd.Series(get_sentiment(x)))
df.to_csv("data/processed/sentiment.csv", index=False)
print(df['sentiment'].value_counts())
print(f"Avg sentiment: {df['sentiment_score'].mean():.3f}")
