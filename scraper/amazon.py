import requests
from bs4 import BeautifulSoup


def get_price(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/125.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    price = soup.find("span", class_="a-price-whole")

    if not price:
        return None
    
    
    return int(
    price.text
    .replace(",", "")
    .replace(".", "")
    .strip()
    )