# map_sentiment.py
def map_sentiments(df):
    sentiment_map = {0: "Negative", 2: "Neutral", 4: "Positive"}
    df["sentiment"] = df["target"].map(sentiment_map)
    return df
