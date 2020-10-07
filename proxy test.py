'''
from selenium import webdriver
import time

PROXY = "209.203.130.51:8080" # IP:PORT or HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://%s' % PROXY)

chrome = webdriver.Chrome(chrome_options=chrome_options)
chrome.get("http://whatismyipaddress.com")
time.sleep(10)
print('lol')
PROXY = "116.203.127.92:3128" # IP:PORT or HOST:PORT

chrome_options.add_argument('--proxy-server=http://%s' % PROXY)
chrome = webdriver.Chrome(chrome_options=chrome_options)
chrome.get("http://whatismyipaddress.com")
'''
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

chromedriver = "./chromedriver" # replace with your browser driver
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

urls = ['http://www.freeproxylists.net/?c=&pt=&pr=&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=90','http://www.freeproxylists.net/?u=90&page=2','http://www.freeproxylists.net/?u=90&page=3']

#count = 1
#while (count < 2):
for url in urls:
 driver.get(url)
 assert "Free Proxy Lists - HTTP Proxy Servers (IP Address, Port)" in driver.title
 data = driver.page_source
 #driver.close()

 soup = BeautifulSoup(data, 'html.parser')
 query = soup.find_all('tbody')

 tulis = query[1]

 soup = BeautifulSoup(str(tulis), 'html.parser')
 query = soup.find_all('tr')
 for t in query:
  td = t.find_all('td')
  if 'IPDecode' in str(td[0]):
   print(td[0].text.split(')')[1]+':'+td[1].text+':'+td[2].text+':'+str(td[8]).split('width:')[1].split(';')[0])
   fil = open('proxy.txt','a')
   fil.write(str(td[0].text.split(')')[1]+':'+td[1].text+':'+td[2].text+':'+str(td[8]).split('width:')[1].split(';')[0]+'\n'))
   fil.close()

 driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

driver.close()
