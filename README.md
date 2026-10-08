# Real-time Streaming Sentiment & Topic Dashboard

Simulates live Twitter/Reviews stream → NLP → Dashboard

## Pipeline
1. Generate 2000 fake social posts for Paystack/Moniepoint/Flutterwave
2. VADER Sentiment (positive/neutral/negative + score)
3. Topic Modeling via TF-IDF + KMeans (auto-discovers pricing/service/product)
4. Streaming aggregates: hourly trends, entity health

## Tech
Python, VADER, Scikit-learn, Streamlit, Plotly, GitHub Actions (every 30 mins)

## How to Run Locally
streamlit run app.py

## Result
Detects sentiment crashes in real-time per brand
