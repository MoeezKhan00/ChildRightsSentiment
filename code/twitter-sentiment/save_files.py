# save_files.py
def save_by_sentiment(df):
    df[df['sentiment'] == 'Positive'].to_csv('positive_tweets.csv', index=False)
    df[df['sentiment'] == 'Negative'].to_csv('negative_tweets.csv', index=False)
