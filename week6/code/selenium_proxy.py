from browsermobproxy import Server
from selenium import webdriver
import json

# create a browsermob server instance
server = Server("browsermob-proxy/bin/browsermob-proxy")
server.start()
proxy = server.create_proxy(params=dict(trustAllServers=True))

# create a new chromedriver instance
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--proxy-server={}".format(proxy.proxy))
chrome_options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chrome_options)

# do crawling
proxy.new_har("myhar")
driver.get("http://www.google.com")
driver.get("http://www.yahoo.com")

# write har file
with open('myhar.har', 'w') as f:
    f.write(json.dumps(proxy.har))

# stop server and exit
server.stop()
driver.quit()