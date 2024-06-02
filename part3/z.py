# list1 = ["a","b","c"]
# list2 = [1,2,3]

# # using zip to combine list1 and list2
# zipped = list(zip(list1,list2))
# print(zipped)

from htmlExtractor import extractHtml

soup = extractHtml("https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets","html.parser")
print(soup)