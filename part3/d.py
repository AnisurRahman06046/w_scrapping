import requests
from bs4 import BeautifulSoup
import pandas as pd 

# request url
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

# response
r = requests.get(url)

# parse the html
soup = BeautifulSoup(r.text,"html.parser")

# get the names,prices and description data
productsNames = soup.find_all("a",class_="title")
productPrices = soup.find_all("h4",class_="price float-end card-title pull-right")
productDes = soup.find_all("p",class_="description card-text")


# make the list of the extracted data 
product_names=[product_name.string for product_name in productsNames]
prices = [price.string for price in productPrices]
desc = [d.string for d in productDes]

df = pd.DataFrame({"Product Names":product_names,"Prices":prices,"Description":desc})
df.to_csv("tablets.csv")
