from bs4 import BeautifulSoup
import requests
# import re
import nltk
import matplotlib.pyplot as plt
from nltk.tokenize import RegexpTokenizer

def plot_word_freq(url):
    r = requests.get(url)
    html = r.text

    soup = BeautifulSoup(html, 'html5lib')
    text = soup.get_text()

    tokenizer = RegexpTokenizer('\w+')
    tokens = tokenizer.tokenize(text)

    words = []
    for word in tokens:
        words.append(word.lower())

    sw = nltk.corpus.stopwords.words('english')

    words_ns = []
    for word in words:
        if word not in sw:
            words_ns.append(word)

    freqdist1 = nltk.FreqDist(words_ns)
    freqdist1.plot(25)


#pride and justice
plot_word_freq('https://www.gutenberg.org/files/42671/42671-h/42671-h.htm')

# robinson crusue
# plot_word_freq('https://www.gutenberg.org/files/521/521-h/521-h.htm')

# moby dick
# plot_word_freq('https://www.gutenberg.org/files/2701/2701-h/2701-h.htm')
