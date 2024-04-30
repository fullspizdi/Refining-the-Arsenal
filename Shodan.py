import requests
from Utilities import log_message, check_internet_connection

# Constants
SHODAN_API_KEY = "YOUR_SHODAN_API_KEY"
SHODAN_BASE_URL = "https://api.shodan.io"

def search_shodan(query):
    """
    Search Shodan with a given query and return the results.
    """
    if not check_internet_connection():
        log_message("Internet connection is required to perform Shodan searches.")
        return None

    url = f"{SHODAN_BASE_URL}/shodan/host/search?key={SHODAN_API_KEY}&query={query}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        results = response.json()
        log_message(f"Shodan search completed for query: {query}")
        return results
    except requests.RequestException as e:
        log_message(f"Failed to perform Shodan search: {e}")
        return None

def print_search_results(results):
    """
    Print the search results from Shodan.
    """
    if results and 'matches' in results:
        for match in results['matches']:
            print(f"IP: {match.get('ip_str')}")
            print(f"Organization: {match.get('org', 'N/A')}")
            print(f"Operating System: {match.get('os', 'N/A')}")
            print("Ports:")
            for port in match.get('ports', []):
                print(f" - {port}")
            print("-" * 40)
    else:
        log_message("No results found or invalid response.")

if __name__ == "__main__":
    query = "apache"
    log_message(f"Initiating Shodan search for: {query}")
    results = search_shodan(query)
    print_search_results(results)
