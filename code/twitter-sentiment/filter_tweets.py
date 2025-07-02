# filter_tweets.py

def filter_relevant_tweets(df):
    keywords = ['child', 'children', 'school', 'education', 'child labor', 'rights', 'abuse', 'vaccination', 'health']
    filtered_df = df[df['text'].str.lower().str.contains('|'.join(keywords), na=False)].copy()
    return filtered_df
