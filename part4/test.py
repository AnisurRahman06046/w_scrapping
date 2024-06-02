from htmlExtractor import extractHtml
soup = extractHtml("https://ticker.finology.in/","html.parser")
print(soup)