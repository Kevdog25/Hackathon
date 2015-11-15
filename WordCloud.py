from wordcloud import WordCloud
import matplotlib.pyplot as plt


def generate_wordcloud(text):
    temp = [' '.join(row) for row in text]
    text = ' '.join(temp)
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
