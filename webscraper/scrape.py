import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github User: ')
url = 'https://github.com/' + github_user
r = requests.get(url)

soup = bs(r.content, 'html.parser')
target = soup.find('img', {'class': 'avatar'})['src']
print(target)