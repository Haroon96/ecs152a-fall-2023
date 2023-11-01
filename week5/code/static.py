import requests
from bs4 import BeautifulSoup

# send a request
static_url = 'https://haroon96.github.io/ecs152a-fall-2023/week5/web/static.html'
dynamic_url = 'https://haroon96.github.io/ecs152a-fall-2023/week5/web/dynamic.html'
r = requests.get(dynamic_url)
html = r.text

# convert to soup object
soup = BeautifulSoup(html, 'html.parser')

# find all images
print("All images by tag")
imgs = soup.find_all('img')
for img in imgs:
    print(img['src'])

# find all blue background images
print("Blue images by class")
blue_imgs = soup.find_all(attrs={'class': 'image-blue'})
for img in blue_imgs:
    print(img['src'])

# find specific images
print("Specific image by ID")
img1 = soup.find(id='img1')
if img1:
    print(img1['src'])