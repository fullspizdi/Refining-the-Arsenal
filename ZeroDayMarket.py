import requests
from bs4 import BeautifulSoup
import logging

class ZeroDayMarket:
    def __init__(self):
        self.market_urls = [
            "https://example-marketplace1.com",
            "https://example-marketplace2.com"
        ]
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

    def fetch_market_data(self):
        """ Fetches data from various zero-day marketplaces """
        zero_day_exploits = []
        for url in self.market_urls:
            try:
                response = requests.get(url, headers=self.headers)
                if response.status_code == 200:
                    zero_day_exploits.extend(self.parse_marketplace(response.text))
                else:
                    logging.error(f"Failed to fetch data from {url}, Status Code: {response.status_code}")
            except Exception as e:
                logging.error(f"Error fetching data from {url}: {str(e)}")
        return zero_day_exploits

    def parse_marketplace(self, html_content):
        """ Parses HTML content of a marketplace to extract zero-day exploit details """
        soup = BeautifulSoup(html_content, 'html.parser')
        exploits = []
        for item in soup.find_all('div', class_='exploit-list-item'):
            title = item.find('h3').text.strip()
            price = item.find('span', class_='price').text.strip()
            exploits.append({'title': title, 'price': price})
        return exploits

    def display_exploits(self, exploits):
        """ Displays the list of zero-day exploits """
        print("Available Zero-Day Exploits:")
        for exploit in exploits:
            print(f"Title: {exploit['title']}, Price: {exploit['price']}")

if __name__ == "__main__":
    zdm = ZeroDayMarket()
    exploits = zdm.fetch_market_data()
    zdm.display_exploits(exploits)
