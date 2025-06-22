import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwordsz')

def count_all_words(book):
    # find all unique words in book
    pattern = re.compile("[a-zA-Z]+")
    # lower is used to make capitalized and noncapitalized version of the same word equal
    findings = re.findall(pattern, book.lower())

    # create dictionary of all words and the number of times they appear in the book
    d = {}
    for word in findings:
        if word in d.keys():
            d[word] = d[word] + 1
        else:
            d[word] = 1

    # convert dict to list, we want value to come first so it sorts by value and not by alphabet
    d_list = [(value, key) for (key, value) in d.items()]
    return sorted(d_list, reverse=True)

def filter_stopwords(word_list):
    english_stopwords = stopwords.words("english")
    filtered_words = []
    for count, word in word_list:
        if word not in english_stopwords:
            filtered_words.append((word, count))
    return filtered_words