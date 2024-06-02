from htmlExtractor import extractHtml

import pandas as pd

soup = extractHtml("https://ticker.finology.in/","html.parser")
print(soup)