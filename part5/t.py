from htmlExtractor import extractHtml
import pandas as pd

soup = extractHtml("https://ticker.finology.in/","html.parser")
table = soup.find("table",class_="table table-sm table-hover screenertable")
table_header = table.find_all("th")
print(len(table_header))
headers = [header.text for header in table_header]
print(headers)

# for i in table_header:
#     print(i.text)