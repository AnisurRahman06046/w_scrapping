from htmlExtractor import extractHtml
import pandas as pd

soup = extractHtml("https://ticker.finology.in/","html.parser")
table = soup.find("table",class_="table table-sm table-hover screenertable")
table_header = table.find_all("th")
print(len(table_header))
headers = [header.text for header in table_header]
# table_datas = table.find_all("td")
# # print(table_datas)
# datas = [data.text for data in table_datas]
# print(datas)

# for i in table_header:
#     print(i.text)

df = pd.DataFrame(columns=headers)
# print(df)

rows = table.find_all("tr")

for i in rows[1:]:
    data = i.find_all("td")
    row = [tr.text.strip() for tr in data]
    l = len(df)
    df.loc[l]=row
    
# print(df)
df.to_csv("tablesData.csv")