# 📖 Book Sentiment & Word Frequency Analyzer

This Python project analyzes a book's sentiment and highlights its most frequent, meaningful words. It processes full-text content, filters out common stopwords, and evaluates sentiment on both the overall and chapter levels using NLTK’s VADER sentiment analyzer.

---

## 🔍 Features

- **Word Frequency Analysis**: Counts and ranks all words in a book by frequency
- **Stopword Filtering**: Removes common English words to highlight key terms
- **Sentiment Analysis**: Gauges emotional tone of the entire book and by chapter
- **Customizable Input**: Plug in any plain-text `.txt` book file

---

## 🛠 Technologies Used

- `nltk` (Natural Language Toolkit)
- `re` (Regular Expressions)
- Python standard libraries: `os`, `file`, `print`

---

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/yourusername/book-analyzer.git
cd book-analyzer

### 2. Install Requirements

pip install nltk

### 3. Add a Book

Place the .txt version of the book you'd like to analyze in the project directory. Update the filename in main.py if needed

📂 File Overview
- main.py: Orchestrates the word count and sentiment analysis workflows
- word_counter.py: Counts words and filters out stopwords
- analyze_sentiment.py: Uses VADER to evaluate polarity of text and chapters
- miracle_in_the_andes.txt: Sample text file for analysi

🌍 Real-World Applications
- Sentiment profiling of novels, speeches, or essays
- Text mining for researchers or analysts
- Comparative literary analysis or curriculum tools
- Author tone tracking across multiple works