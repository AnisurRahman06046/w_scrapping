import requests 
from bs4 import BeautifulSoup
url = "https://www.geeksforgeeks.org/python-programming-language/"
# make a get request
r = requests.get(url)

# check status code for response received
print(r)

# print the content of request
# print(r.content)

# parsing the html
soup = BeautifulSoup(r.content,'html.parser')
# print(soup.prettify())

s = soup.find("div",class_="entry-content")
content = s.find_all("p")
print(content)

for line in content:
    print(line.text)