import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
       response = requests.get(url)
       soup = BeautifulSoup(response.text, 'html.parser')

       # Extract quotes and authors
       quotes = soup.select('.quote .text')
       authors = soup.select('.quote .author')

       # Display and save quotes to a file
       with open('quotes.txt', 'w', encoding='utf-8') as file:
           for quote, author in zip(quotes, authors):
               print(f"{quote.get_text()} - {author.get_text()}")
               file.write(f"{quote.get_text()} - {author.get_text()}\n")

if __name__ == "__main__":
       # Specify the URL to scrape
       target_url = 'http://quotes.toscrape.com'
       
       # Call the scrape_quotes function
       scrape_quotes(target_url)