import pandas as pd
from datetime import datetime

df = pd.read_csv("data/processed/topics.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Hourly sentiment trend per entity
df['hour'] = df['timestamp'].dt.floor('H')
trend = df.groupby(['hour','entity','sentiment']).size().reset_index(name='count')
trend.to_csv("data/processed/trend.csv", index=False)

# Entity health score
health = df.groupby('entity')['sentiment_score'].mean().reset_index()
health.to_csv("data/processed/entity_health.csv", index=False)
print("Streaming aggregates ready")
print(health)
