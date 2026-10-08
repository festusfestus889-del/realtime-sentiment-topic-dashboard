import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import os

df = pd.read_csv("data/processed/sentiment.csv")

# TF-IDF + KMeans = simple topic model that works
vectorizer = TfidfVectorizer(stop_words='english', max_features=100)
X = vectorizer.fit_transform(df['text'])

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['topic_cluster'] = kmeans.fit_predict(X)

# Get top words per cluster
terms = vectorizer.get_feature_names_out()
for i in range(3):
  center = kmeans.cluster_centers_[i]
  top = [terms[idx] for idx in center.argsort()[-5:][::-1]]
  print(f"Cluster {i}: {', '.join(top)}")

df.to_csv("data/processed/topics.csv", index=False)
