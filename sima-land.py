import requests, csv
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text

def get_total_page(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='b-pagination').find_all('a', class_='b-pagination__page')[-1].get('href')
    total_pages = pages.split('p')[1].split('/')[0]

    return int(total_pages)

def write_csv(date):
    with open('spisok.csv', 'a') as f:
        write = csv.writer(f)

        write.writerow( (date['title'],
                          date['url'],
                          date['price'],
                          date['info']) )




def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='catalog__list').find_all('div', class_='catalog__item-main')

    for ad in ads:
        try:
            title = ad.find('div', class_='catalog__item-details delivery-details').find(class_='link').text.strip()
        except:
            title = ''
        try:
            url = 'https://sima-land.ru' + ad.find('div', class_='catalog__item-details delivery-details').find('a').get('href')

        except:
            url = ''

        try:
            price = ad.find('div', class_='catalog__item-price ').find(class_='price__val').text
        except:
            price = ''

        try:
            html = get_html(url)
            sup = BeautifulSoup(html, 'lxml')
            info = sup.find('li', class_='b-properties__header').text

        except:
            info = ''


        data = {'title':title,
                'url':url,
                'price':price,
                'info':info}

        write_csv(data)




def main():
    url = 'https://www.sima-land.ru/igrushki/razvivayuschie-i-obuchayuschie-igrushki/p3/'
    base_url = 'https://www.sima-land.ru/igrushki/razvivayuschie-i-obuchayuschie-igrushki/'
    page_part = 'p'
    total_pages = get_total_page(get_html(url))
    for i in range(1):
        url_gen = base_url + page_part + str(i)
        html = get_html(url_gen)
        get_page_data(html)








if __name__ == '__main__':
    main()