from htmlExtractor import extractHtml
import pandas as pd 


soup = extractHtml("https://www.iplt20.com/auction/2024","html.parser")
table = soup.find("table",class_="ih-td-tab auction-tbl",id="t4")
t_h = table.find_all("th")
# print(headers)
headers = [t.text.strip() for t in t_h]
# print(headers)
df = pd.DataFrame(columns=headers)
# print(df)
tb = table.find("tbody",id="pointsdata")
t_r = tb.find_all("tr")
# print(t_r)
# datas = [d.text.strip().replace('\n', ' ') for d in t_r]
for row in t_r:
    cols = row.find_all("td")
    # print(cols)
    data = [col.text.replace('\n', ' ').replace('₹', '').strip() for col in cols]  # Remove newline characters and strip whitespace
    df.loc[len(df)] = data  # Add the cleaned data to the DataFrame

print(df)

# df.to_csv("ipl_auction.csv")
df.to_csv("auction.csv")


