import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException, Timeout, TooManyRedirects

def get_definition(word):
    try:
        url = f"https://www.merriam-webster.com/dictionary/{word}"
        response = requests.get(url, timeout=10)  # Set a timeout of 10 seconds
        response.raise_for_status()  # Raises an HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        definition_elem = soup.find('span', class_='dtText')
        if definition_elem:
            return definition_elem.text.strip()
        else:
            print(f"Definition element not found for word: {word}")
            return "Definition not found."
    except Timeout:
        print(f"Request timed out while fetching definition for: {word}")
        return "Error: Request timed out. Please try again later."
    except TooManyRedirects:
        print(f"Too many redirects while fetching definition for: {word}")
        return "Error: Too many redirects. Please try again later."
    except RequestException as e:
        print(f"An error occurred while fetching the definition: {str(e)}")
        return f"Error fetching definition: {str(e)}"