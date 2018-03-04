import requests
from bs4 import BeautifulSoup
'''
План работ :
1) ВЫяснить количество страниц (опередить) которые будем парсить
2) Сортировать список URL страниц товаров
3) Собрать данные 
'''


def get_html(url):
    r = requests.get(url)
    return r.text

def get_total_page(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='b-pagination').find_all('a', class_='b-pagination__page')[-1].get('href')
    total_pages = pages.split('p')[1].split('/')[0]

    return int(total_pages)




def main():
    url = 'https://www.sima-land.ru/igrushki/razvivayuschie-i-obuchayuschie-igrushki/p3/'
    base_url = 'https://www.sima-land.ru/igrushki/razvivayuschie-i-obuchayuschie-igrushki/'
    page_part = 'p'
    total_pages = get_total_page(get_html(url))
    for i in range(1, 90):
        url_gen = base_url + page_part + str(i)
        print(url_gen)






if __name__ == '__main__':
    main()