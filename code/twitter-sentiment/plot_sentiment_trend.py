# plot_sentiment_trend.py
import pandas as pd
import matplotlib.pyplot as plt  # ✅ Not: import matplotlib


def plot_sentiment_trend(df):
    sentiment_trend = df.set_index('date').groupby([pd.Grouper(freq='W'), 'sentiment']).size().unstack().fillna(0)
    sentiment_trend.plot(figsize=(12,6), marker='o')
    plt.title("Sentiment Trend Over Time")
    plt.xlabel("Week")
    plt.ylabel("Tweet Count")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('sentiment_trend.png')
    plt.close()
