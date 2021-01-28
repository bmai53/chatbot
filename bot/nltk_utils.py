import nltk
from nltk.stem.snowball import SnowballStemmer
import numpy as np

# nltk.download('punkt')
stemmer = SnowballStemmer("english")


def tokenize(sentence):
    return nltk.word_tokenize(sentence)


def stem(word):
    return stemmer.stem(word.lower())  # remove suffixes


def bag_of_words(tokenized_sentence, all_words):
    """
    Example:
        sentence  =   ['hello', 'how', 'are', 'you']
        words     =   ['hi', 'hello', 'I', 'you', 'bye', 'thank', 'cool']
        bag       =   [ 0,    1,       0,     1,     0,       0,      0]
    """

    tokenized_sentence = [stem(w) for w in tokenized_sentence]

    bag = np.zeros(len(all_words), dtype=np.float32)

    for i, w, in enumerate(all_words):
        if w in tokenized_sentence:
            bag[i] = 1.0

    return bag
