# plot_sentiment_distribution.py
import matplotlib.pyplot as plt

def plot_sentiment_distribution(df):
    sentiment_dist = df.groupby('theme')['sentiment'].value_counts(normalize=True).unstack().fillna(0)
    sentiment_dist.plot(kind='bar', stacked=True, figsize=(12,6), colormap='coolwarm')
    plt.title("Sentiment Distribution by Theme")
    plt.xlabel("Theme")
    plt.ylabel("Proportion")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('sentiment_distribution_by_theme.png')
    plt.close()
