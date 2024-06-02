import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text,"html.parser")
products = soup.find_all("a",class_="title")
prices = soup.find_all("h4",class_="price float-end card-title pull-right")
desc = soup.find_all("p",class_="description card-text")
# print(products)
for product in products:
    print(product.string)
    
for price in prices:
    print(price.string)
    
for d in desc:
    print(d.string)