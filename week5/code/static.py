import requests
from bs4 import BeautifulSoup

# send a request
static_url = 'https://haroon96.github.io/ecs152a-fall-2023/week5/web/static.html'
r = requests.get(static_url)
html = r.text

# convert to soup object
soup = BeautifulSoup(html, 'html.parser')

# find all images
imgs = soup.find_all('img')
for img in imgs:
    print(img['src'])