import analyze_sentiment
import word_counter



with open('miracle_in_the_andes.txt', 'r', encoding='utf-8') as file:
    book = file.read()

word_count_list = word_counter.count_all_words(book)

filtered_words = word_counter.filter_stopwords(word_count_list)

print(f"The most common, non stop word is {filtered_words[0][0]} at a count of {filtered_words[0][1]} times")

print(analyze_sentiment.analyze_book_polarity(book))

print(analyze_sentiment.analyze_chapter_polarity(book))
