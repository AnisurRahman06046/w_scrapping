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

rows = table.find_all("tr")
for i in rows[1:]:
    # # print(i)
    tr = i.find_all("td")
    # # print(tr)
    row = [data.text.strip() for data in tr]
    l = len(df)
    df.loc[l]=row

# print(rows)
print(df)

df.to_csv("table_data.csv")