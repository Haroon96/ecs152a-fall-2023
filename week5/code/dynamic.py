from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

# create a webdriver
driver = Chrome()

# load page URL
dynamic_url = 'https://haroon96.github.io/ecs152a-fall-2023/week5/web/dynamic.html'
driver.get(dynamic_url)

# click on add button
add_btn = driver.find_element(By.XPATH, '//*[@id="add_btn"]')
for _ in range(20):
    add_btn.click()
    sleep(1)
    
# find all images
print("All images by tag")
imgs = driver.find_elements(By.TAG_NAME, 'img')
for img in imgs:
    print(img.get_attribute('src'))

# find all blue background images
print("Blue images by class")
blue_imgs = driver.find_elements(By.CLASS_NAME, 'image-blue')
for img in blue_imgs:
    print(img.get_attribute('src'))

# find specific images
print("Specific image by ID")
img1 = driver.find_element(By.ID, 'img1')
if img1:
    print(img1.get_attribute('src'))

input()