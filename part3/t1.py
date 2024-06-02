import requests
from bs4 import BeautifulSoup
import csv
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text,"html.parser")
products = soup.find_all("a",class_="title")
prices = soup.find_all("h4",class_="price float-end card-title pull-right")
desc = soup.find_all("p",class_="description card-text")
# print(products)
# for product in products:
#     print(product.string)
    

    
# for price in prices:
#     print(price.string)
    
# for d in desc:
#     print(d.string)

product_names = [product.string for product in products]
product_prices = [price.string for price in prices]
product_desc = [ds.string for ds in desc]


csv_file='products.csv'
with open(csv_file,mode='w',newline="",encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Product_Name","Price","Description"])
    for name,price,dsc in zip(product_names,product_prices,product_desc):
        writer.writerow([name,price,dsc])