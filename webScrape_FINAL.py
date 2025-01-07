import requests
from bs4 import BeautifulSoup
import spacy
import concurrent.futures
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def scrape_sentences_with_word(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    search_word = input(f"Enter a word to find sentences containing it: ").lower()
    nlp = spacy.load("en_core_web_sm")
    result = []
    for paragraph in paragraphs:
        doc = nlp(paragraph.get_text())
        for sentence in doc.sents:
            if search_word in sentence.text.lower():
                result.append(sentence.text.strip())
    return result

def scrape_words_by_length(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    words = soup.get_text().split()
    word_length = int(input(f"Enter the character length of words to display: "))
    filtered_words = [word for word in words if len(word) == word_length]
    return filtered_words

def analyze_and_visualize(words_list):
    word_counts = Counter(words_list)
    df = pd.DataFrame.from_dict(word_counts, orient='index', columns=['Frequency'])
    df = df.sort_values(by='Frequency', ascending=False)
    # Convert the index (words) to string to ensure numeric values
    df.index = df.index.astype(str)
    if not df.empty:
        # Plot a line chart using word frequencies
        df['Frequency'].plot(kind='line', marker='o', linestyle='-', color='green')
        plt.title('Word Frequency Distribution')
        plt.xlabel('Words')
        plt.ylabel('Frequency')
        plt.show()
    else:
        print("No words of the specified length found.")
if __name__ == "__main__":
    target_url = input("Enter the URL to scrape: ")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Parallelize the execution of the functions for each URL
        sentences_result = list(executor.map(scrape_sentences_with_word, [target_url]))
        words_result = list(executor.map(scrape_words_by_length, [target_url]))
    # Flatten the results from parallel execution
    sentences_list = [sentence for sublist in sentences_result for sentence in sublist]
    words_list = [word for sublist in words_result for word in sublist]
    # Display sentences containing the specified word
    print("\nSentences containing the specified word:\n")
    for sentence in sentences_list:
        print(sentence)
    # Display words of the specified length
    print("\nWords of the specified length:\n")
    for word in words_list:
        print(word)
    # Analyze and visualize word frequency
    analyze_and_visualize(words_list)
