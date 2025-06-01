import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()

def analyze_polarity(text):
    polarity = analyzer.polarity_scores(text)
    compound_score = polarity["compound"]
    if compound_score > 0:
        return "This is a positive text"
    elif compound_score == 0:
        return "This text is neutral"
    else:
        return "This is a negative text"

def analyze_book_polarity(book):
    return analyze_polarity(book)

def analyze_chapter_polarity(book):
    pattern = re.compile("Chapter [0-9]+")
    chapters = re.split(pattern, book)
    scores = []
    for index, chapter in enumerate(chapters[1:]):
        scores.append((f"Chapter {index}+1", analyze_polarity(chapter)))
    return scores