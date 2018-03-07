import requests
from bs4 import BeautifulSoup

url = 'https://www.deviantart.com/newest/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

test = soup.find(id='browse-results-page-1').find_all(class_='artist')
b = str()
c = open('links.txt', 'r')
file = str(c.readlines())
c.close()
for sup in test:
    user = sup.find('a').get('href')
    if user in file:
        continue
    else:
        a = str(user) + '\n'
        b += a

c = open('links.txt', 'a')
c.writelines(b)
c.close()



