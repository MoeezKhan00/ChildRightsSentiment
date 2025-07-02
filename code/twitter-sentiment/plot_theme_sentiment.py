# plot_theme_sentiment.py
# import pandas as pd
import matplotlib.pyplot as plt

def plot_theme_by_sentiment(df):
    theme_sentiment = df.groupby(['theme', 'sentiment']).size().unstack().fillna(0)
    theme_sentiment.plot(kind='bar', figsize=(12,6))
    plt.title("Tweet Themes by Sentiment")
    plt.xlabel("Theme")
    plt.ylabel("Tweet Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('tweet_theme_by_sentiment.png')
    plt.close()
