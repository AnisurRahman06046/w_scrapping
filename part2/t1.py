import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone"
r = requests.get(url)
# soup = BeautifulSoup(r.text,"html.parser")
soup = BeautifulSoup(r.text,"lxml")
# print(soup.div.p)
tag = soup.header 
print(tag.attrs['role'])