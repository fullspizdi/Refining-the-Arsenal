import logging
from ZeroDayMarket import ZeroDayMarket

class ZeroDayResearch:
    def __init__(self):
        self.zero_day_market = ZeroDayMarket()

    def research_exploits(self):
        """ Researches zero-day exploits by fetching data from marketplaces """
        try:
            exploits = self.zero_day_market.fetch_market_data()
            self.analyze_exploits(exploits)
        except Exception as e:
            logging.error(f"Error during research: {str(e)}")

    def analyze_exploits(self, exploits):
        """ Analyzes the fetched exploits for potential use and value """
        valuable_exploits = [exploit for exploit in exploits if self.is_valuable(exploit)]
        print("Valuable Zero-Day Exploits:")
        for exploit in valuable_exploits:
            print(f"Title: {exploit['title']}, Price: {exploit['price']}")

    def is_valuable(self, exploit):
        """ Determines if an exploit is valuable based on certain criteria """
        # Example criteria: price below a certain amount or specific keywords in title
        price_limit = 10000  # hypothetical price limit
        valuable_keywords = ['remote', 'RCE', 'escalation']
        price = int(exploit['price'].replace('$', '').replace(',', ''))
        for keyword in valuable_keywords:
            if keyword.lower() in exploit['title'].lower() and price <= price_limit:
                return True
        return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    zdr = ZeroDayResearch()
    zdr.research_exploits()
