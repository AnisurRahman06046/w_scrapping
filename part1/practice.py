import requests 

# make a request
url = "https://authoraditiagarwal.com/"
r = requests.get(url)
print(r.text[:200])