import requests
from bs4 import BeautifulSoup

response = requests.get('https://example.com')
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
for link in links:
    if link.get('href'):
        print(link.get('href'))
