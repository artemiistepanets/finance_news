import requests
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def scrape_yahoo_finance_news(ticker_symbol):
    base_url = f'https://finance.yahoo.com/quote/{ticker_symbol}/news?p={ticker_symbol}'
    
    # Send an HTTP GET request to the URL
    response = requests.get(base_url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'lxml')
        
        # Extract news articles
        articles = soup.find_all('li', {'data-test': 'media-item'})
        
        # Initialize SentimentIntensityAnalyzer
        sid = SentimentIntensityAnalyzer()
        
        for article in articles:
            # Extract relevant information (title and link)
            title = article.find('h3').text
            link = article.find('a')['href']
            
            # Perform sentiment analysis on the article title
            sentiment_score = sid.polarity_scores(title)['compound']
            
            print(f'Title: {title}\nLink: {link}\nSentiment Score: {sentiment_score}\n\n')
    else:
        print(f'Error: Unable to fetch data. Status code: {response.status_code}')

# Example usage
ticker_symbol = 'AAPL'  # Replace with the desired stock symbol
scrape_yahoo_finance_news(ticker_symbol)
