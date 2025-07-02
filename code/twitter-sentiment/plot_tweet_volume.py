import matplotlib.pyplot as plt
import pandas as pd

def plot_daily_volume(df):
    # Make sure date column is datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])

    # Set date as index and group
    df = df.set_index('date')

    # Resample by day and group by theme
    grouped = (
      df.groupby(['theme', pd.Grouper(freq='D')], group_keys=False)
      .size()
      .unstack(level=0)
      .fillna(0)
)


    # Unstack to get themes as columns
    daily = grouped.unstack(level=0).fillna(0)

    # Plot
    daily.plot(figsize=(12, 6))
    plt.title("Daily Tweet Volume by Theme")
    plt.xlabel("Date")
    plt.ylabel("Number of Tweets")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
