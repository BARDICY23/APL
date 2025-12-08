import requests
from bs4 import BeautifulSoup
import csv
from io import StringIO
import re
def fetch_title(url):
    r = requests.get(url)
    s = BeautifulSoup(r.text, 'html.parser')
    return s.title.string.strip()
def extract_links(url):
    r = requests.get(url)
    s = BeautifulSoup(r.text, 'html.parser')
    return [a['href'] for a in s.find_all('a', href=True)]
def extract_table(html):
    s = BeautifulSoup(html, 'html.parser')
    rows = []
    for tr in s.find_all('tr'):
        cols = [td.get_text(strip=True) for td in tr.find_all(['th','td'])]
        rows.append(cols)
    return rows
def save_fruits(html, outpath='fruits.csv'):
    s = BeautifulSoup(html, 'html.parser')
    items = [li.get_text(strip=True) for li in s.find_all('li')]
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['Fruit'])
        for it in items:
            w.writerow([it])
if __name__ == '__main__':
    print(fetch_title('https://example.com'))
    print(extract_links('https://example.com'))
    html = '<table>\n  <tr><th>Name</th><th>Age</th></tr>\n  <tr><td>Alice</td><td>28</td></tr>\n  <tr><td>Bob</td><td>30</td></tr>\n</table>'
    print(extract_table(html))
    fruits_html = '<ul>\n  <li>Apple</li>\n  <li>Banana</li>\n  <li>Cherry</li>\n</ul>'
    save_fruits(fruits_html)
