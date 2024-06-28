import requests
from bs4 import BeautifulSoup

def gbooks(r, b):
    response = requests.get(f"https://www.google.com/search?q={r}&tbm=bks")
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('div', {'class': 'BNeawe vvjwJb AP7Wnd'})[b]
    return books.get_text()