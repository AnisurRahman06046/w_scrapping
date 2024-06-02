import requests
import pandas as pd 
from bs4 import BeautifulSoup

def fetchHtml(webiste,parser):
    url = webiste
    r = requests.get(url)
    soup_data = BeautifulSoup(r.text,parser)
    return soup_data


soup = fetchHtml("https://ticker.finology.in/","html.parser")
print(soup.prettify())