from bs4 import BeautifulSoup
from .model import Volkswagen
import requests

for page_number in range(1, 3):
    # There is 563 pages. 

    url = f"https://www.otomoto.pl/osobowe/volkswagen?page={page_number}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    prices = soup.find_all('span', attrs={'class': 'ooa-1bmnxg7 eayvfn611'})

    for price in prices:
        print(price.text)