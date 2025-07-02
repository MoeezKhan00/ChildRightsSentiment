# main.py
from libraries import *
from load_data import load_csv
from filter_tweets import filter_relevant_tweets
from classify_theme import classify_themes
from map_sentiment import map_sentiments
from save_files import save_by_sentiment
import matplotlib.pyplot as plt
import pandas as pd
from plot_tweet_volume import plot_daily_volume
from plot_sentiment_trend import plot_sentiment_trend
from plot_theme_sentiment import plot_theme_by_sentiment
from plot_sentiment_distribution import plot_sentiment_distribution
from plot_wordcloud import generate_wordcloud
from export_final_filtered import export_final_filtered
import os
# Get the base directory (ChildRightsSentiment)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Path to CSV in the /data folder
CSV_PATH = os.path.join(BASE_DIR, 'data', '1.6miltweets.csv')

# Load the CSV
df = load_csv(CSV_PATH)


# Filter relevant tweets
filtered_df = filter_relevant_tweets(df)

# Classify tweet themes
filtered_df = classify_themes(filtered_df)

# Map sentiment values to labels
filtered_df = map_sentiments(filtered_df)

# Save positive and negative tweets to CSV
save_by_sentiment(filtered_df)

# Convert date for time-based analysis
# Remove unrecognized timezone abbreviations like 'PDT', then parse
filtered_df['date'] = (
    filtered_df['date']
    .str.replace(r"\s[P|M|E|C]DT", "", regex=True)  # remove PDT, EDT, etc.
    .pipe(pd.to_datetime, errors='coerce')
)


# Plot visuals
plot_daily_volume(filtered_df)
plot_sentiment_trend(filtered_df)
plot_theme_by_sentiment(filtered_df)
plot_sentiment_distribution(filtered_df)
generate_wordcloud(filtered_df, 'Education')

# Export final CSV
export_final_filtered(filtered_df)
