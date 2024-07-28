from collections import Counter
import re
import openiti.helper.ara

def get_arabic_words(text):
    arabic_words = []
    # Match Arabic Unicode characters (basic and extended Arabic blocks)
    arabic_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+')
    words = re.findall(arabic_pattern, text)
    for word in words:
        # Normalize the arabic words
        cleaned_word = openiti.helper.ara.normalize_ara_heavy(word)
        arabic_words.append(cleaned_word)
    return arabic_words

def count_and_sort_words(words):
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(100)
    return most_common_words

def main():
    file_path = 'WZATB.txt'  # Replace with your text file path
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    arabic_words = get_arabic_words(text)
    most_common_arabic_words = count_and_sort_words(arabic_words)

    print("100 Most Common Arabic Words:")
    for word, count in most_common_arabic_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
