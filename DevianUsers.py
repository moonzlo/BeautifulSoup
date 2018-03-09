import requests, time
from bs4 import BeautifulSoup


def parsing():
    set = int(0)
    # Собираем из 4х страниц Url'ы всех пользователей (около 22 с каждой)
    links = ['https://www.deviantart.com/digitalart/newest/',
             'https://www.deviantart.com/traditional/newest/',
             'https://www.deviantart.com/photography/newest/',
             'https://www.deviantart.com/manga/newest/']
    while set != int(4):
        r = requests.get(links[set])
        soup = BeautifulSoup(r.text, 'lxml')

        test = soup.find(id='browse-results-page-1').find_all(class_='artist')
        b = str()
        c = open('links.txt', 'r')
        file = str(c.readlines())
        c.close()
        for sup in test:  # Реализуем проверку каждой ссылки на наличие её в Уже сформированном листе.
            user = sup.find('a').get('href')
            if user in file:  # Если ссылка есть в списке, она игнорируется.
                continue
            else:
                a = str(user) + '\n'  # Данная кострукция реализована с целью последовательной записи в новую строку.
                b += a  # К данной кострукции пришлось прибегнуть по причине неверной записи ссылок.

        c = open('links.txt', 'a')  # Осуществляем запись в файл (он должен быть создан).
        c.writelines(b)  # Посторочно записываем содержимое переменной с сылками.
        c.close()
        set += int(1)  # Конструкция для перебора донорских ссылок.


b = range(1, 10)
for i in b:  # реализация долгосрочного сбора, с интервалом в 10 минут.
    time.sleep(600)
    parsing()
