import pandas as pd 
from htmlExtractor import extractHtml

soup = extractHtml("https://ticker.finology.in/","html.parser")
# print(soup)
table = soup.find("table",class_="table table-sm table-hover screenertable")
# print(table)
table_headers = table.find_all("th")
headers = [header.text for header in table_headers]
# print(headers)

df = pd.DataFrame(columns=headers)
# print(df)