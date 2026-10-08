import pandas as pd, numpy as np, os, random, time
from datetime import datetime, timedelta
os.makedirs("data/raw", exist_ok=True)

topics = {
 "pricing": ["price too high", "expensive", "affordable", "cheap", "cost"],
 "service": ["support was slow", "great service", "rude staff", "helpful", "customer care"],
 "product": ["app crashes", "love the new feature", "buggy", "amazing ui", "update broke it"]
}
sentiments = ["I hate", "I love", "Worst", "Best", "Not bad"]

rows=[]
for i in range(2000):
  entity = random.choice(["Paystack", "Moniepoint", "Flutterwave"])
  topic = random.choice(list(topics.keys()))
  text = f"{random.choice(sentiments)} {entity} {random.choice(topics[topic])} today!"
  rows.append({
    "timestamp": datetime.now() - timedelta(minutes=random.randint(0, 1440)),
    "entity": entity,
    "topic_true": topic,
    "text": text
  })

pd.DataFrame(rows).to_csv("data/raw/stream.csv", index=False)
print("Generated 2000 social posts")
