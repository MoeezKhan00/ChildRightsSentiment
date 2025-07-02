# plot_wordcloud.py

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(df, theme):
    # Join all text under the specified theme into one string
    text_data = ' '.join(df[df['theme'] == theme]['text'].dropna().tolist())
    
    # Generate the word cloud
    wordcloud = WordCloud(width=1000, height=500, background_color='white').generate(text_data)
    
    # Plot the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f'WordCloud for Theme: {theme}')
    plt.axis('off')
    plt.tight_layout()
    
    # Save the image
    plt.savefig(f'wordcloud_{theme.lower()}.png')
    plt.close()
