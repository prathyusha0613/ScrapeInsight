import requests
from bs4 import BeautifulSoup

def scrape_sentences_with_word(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get all sentences
    sentences = soup.find_all('span', class_='text')

    # Ask user for a word to search
    search_word = input("Enter a word to find sentences containing it: ").lower()

    # Display sentences containing the specified word
    for sentence in sentences:
        if search_word in sentence.get_text().lower():
            print(sentence.get_text())

def scrape_words_by_length(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get all words
    words = soup.get_text().split()

    # Ask user for the character length of a word
    word_length = int(input("Enter the character length of words to display: "))

    # Display words of the specified length
    filtered_words = [word for word in words if len(word) == word_length]
    print(filtered_words)

if __name__ == "__main__":
    # Specify the URL to scrape
    target_url = 'http://quotes.toscrape.com'

    # Call the scrape_sentences_with_word function
    scrape_sentences_with_word(target_url)

    # Call the scrape_words_by_length function
    scrape_words_by_length(target_url)
