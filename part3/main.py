import requests 
from bs4 import BeautifulSoup 

url = "https://www.wstech.com/"

r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')
# print(soup)
t = (soup.find("div",class_="et_pb_text_inner"))
print(t.string)
