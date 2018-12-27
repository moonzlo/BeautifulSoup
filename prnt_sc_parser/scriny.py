import requests, randomizer, time
from bs4 import BeautifulSoup

# юезер агент, без него работать не будет!
headers = {
    'authority': 'prnt.sc',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

# Принимает ссылку, отдаёт html код
def get_html(url):
    r = requests.get(url, headers=headers)
    return r.text
# Принимает html и число(имя файла)
def get_total_page(html, num):
    # Объект класса супа, для поиска внутри html
    soup = BeautifulSoup(html, 'html.parser')

    # Находим в коде тег a на котором висит url
    img_url = soup.find_all('a')
    # Проходим по всем a внутри кода, что бы найти нужный href
    for i in img_url:
        # Убираем префикс домена (хз почему он вообще в коде есть), думаю для поиска дубликата.
        noy = 'http://www.google.com/'
        # Патерн для выявления пустышки (пустого url без фото)
        block = 'st.prntscr.com'
        a = i.get('href')
        # Условие по выявлению стариц с содержанием фото.
        if noy in str(a):
            # Условие по отсеиванию реальных фото на заглушек.
            if block not in a:
                # Отделяем ссылку от мусора, путём замены её части.
                valu = str(a.replace('http://www.google.com/searchbyimage?image_url=', ''))
                # Сохраняем изображение (другие методы не будут работать из-за юзер агента)
                with open(r'img\{}.jpg'.format(num), 'wb') as file:
                    # Исходный формат png но я решил что jpg будет меньше весить.
                    file.write(requests.get(valu).content)
                    print('Записал')
                    # ждём секунду, что бы не попасть в бан.
                    time.sleep(1)
                # Возвращаем тру, для движения счётчика. (для смены названия файла)
                return True

            else:
                break
        else:
            continue




#no_img = 'st.prntscr.com/2018/10/13/2048/img/0_173a7b_211be8ff.png'

# Счётчик для смены имени файла.
file_name = int(1)


# Запускаем.
if __name__ == '__main__':
    for i in range(1, 1000):
        try:
            a = get_total_page(get_html(randomizer.get_random_url()), file_name)
            if a == True:
                file_name += 1
        # Ловим ошибки (бывают при большом количестве обращений)
        except Exception as error:
            print(error)
            # делаем перерыв.
            time.sleep(100)
            continue
