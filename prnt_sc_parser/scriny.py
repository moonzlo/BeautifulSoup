import requests, randomizer, time
from bs4 import BeautifulSoup
import urllib.request

headers = {
    'authority': 'prnt.sc',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

#Парсер фото с prnt.sc



def get_html(url):
    r = requests.get(url, headers=headers)
    return r.text

def get_total_page(html, num):
    soup = BeautifulSoup(html, 'html.parser')

    img_url = soup.find_all('a')
    for i in img_url:
        noy = 'http://www.google.com/'
        block = 'st.prntscr.com'
        a = i.get('href')
        if noy in str(a):
            if block not in a:
                valu = str(a.replace('http://www.google.com/searchbyimage?image_url=', ''))
                with open(r'img\{}.jpg'.format(num), 'wb') as file:
                    file.write(requests.get(valu).content)
                    print('Записал')
                    time.sleep(1)
                print(num)
                break
            else:
                break
        else:
            continue




no_img = 'st.prntscr.com/2018/10/13/2048/img/0_173a7b_211be8ff.png'


file_name = int(1)

for i in range(1, 1000):
    try:
        get_total_page(get_html(randomizer.get_random_url()), file_name)
        file_name += 1
        print(i)
    except Exception as error:
        print(error)

