import requests
from bs4 import BeautifulSoup

# url = "https://webscraper.io/test-sites/e-commerce/allinone"
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
# soup = BeautifulSoup(r.text,"html.parser")
soup = BeautifulSoup(r.text,"lxml")
# print(soup.div.p)
# tag = soup.header 
# # print(tag.attrs['role'])
# li = tag.attrs['class']
# print(li)
# for l in li:
#     print(l)

price = (soup.find("h4",{"class":"price float-end card-title pull-right"}))
title = (soup.find("a",{"class":"title"}))
print(price.string)
print(title.string)