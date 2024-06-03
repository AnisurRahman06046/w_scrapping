from htmlExtractor import extractHtml
import pandas as pd 


soup = extractHtml("https://www.iplt20.com/auction/2024","html.parser")
table = soup.find("table",class_="ih-td-tab auction-tbl",id="t4")
t_h = table.find_all("th")
# print(headers)
headers = [t.text.strip() for t in t_h]
print(headers)
df = pd.DataFrame(columns=headers)
print(df)



