import requests
from bs4 import BeautifulSoup

def scrape_sentences_with_word(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get all paragraphs
    paragraphs = soup.find_all('p')

    # Ask user for a word to search
    search_word = input("Enter a word to find sentences containing it: ").lower()

    # Display sentences containing the specified word
    for paragraph in paragraphs:
        sentences = paragraph.text.split('.')
        for sentence in sentences:
            if search_word in sentence.lower():
                print(sentence.strip() + '.')

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
    target_url = 'https://en.wikipedia.org/wiki/Vincent_van_Gogh'

    # Call the scrape_sentences_with_word function
    scrape_sentences_with_word(target_url)

    # Call the scrape_words_by_length function
    scrape_words_by_length(target_url)
