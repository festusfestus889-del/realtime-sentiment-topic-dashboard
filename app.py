import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Real-time Sentiment Dashboard", layout="wide")
st.title("🔴 Real-time Sentiment & Topic Dashboard")

df = pd.read_csv("data/processed/topics.csv")
trend = pd.read_csv("data/processed/trend.csv")
health = pd.read_csv("data/processed/entity_health.csv")

col1, col2, col3 = st.columns(3)
col1.metric("Total Posts", len(df))
col2.metric("Negative %", f"{(df.sentiment=='negative').mean()*100:.1f}%")
col3.metric("Avg Health", f"{health.sentiment_score.mean():.2f}")

st.plotly_chart(px.line(trend, x='hour', y='count', color='sentiment', facet_col='entity', title="Sentiment Trend by Hour"))
st.plotly_chart(px.bar(health, x='entity', y='sentiment_score', color='entity', title="Entity Health Score"))
st.dataframe(df.tail(50))
