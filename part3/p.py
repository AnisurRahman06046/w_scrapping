import requests
from bs4 import BeautifulSoup
import re 


# url = "https://www.amazon.com/SAMSUNG-Smartphone-Unlocked-Android-Processor/dp/B0CMDL3H3V/ref=sr_1_1?dib=eyJ2IjoiMSJ9.Asc6hR4gNWBb-FtA2Mf1ceXsoIxonzYz7QY2hpFtuCAPlswTVpfTQ_8uKijKou8ym6NCqcDPesuWwVsDCVzWPgUj24YFWs5gbOw1Z4Nzol0a7jrZgDbKQcSCSubcPONZ_gwe06CZsz5MPMFbW_gB0OEHrM98XuFqGRAkXvyvisg4PGKkJiIsI-76p7STLmlsLKQRV2Pvikr2qWtDN3uk9m5APFuFlkrdlZHkUBDRr10.EeyemIxGxMT_5P8CSWsuLOFZdVNBD6wVYo_48SaN95A&dib_tag=se&keywords=mobile%2Bphones&qid=1717314549&sr=8-1&th=1"

url='https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'

r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")

names = soup.find_all(string=re.compile("Idea"))
print(len(names))
all_n = [name.string for name in names]
print(all_n)