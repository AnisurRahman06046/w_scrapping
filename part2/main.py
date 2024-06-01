import requests 
url = 'https://www.wstech.com/'
url1 = ''
r = requests.get(url)
print(r.status_code)
print(r.text)