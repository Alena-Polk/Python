import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    res = requests.get(url)
    return res.text


def write_csv(info):
    with open('trial.csv', 'a', encoding='utf-8-sig', newline='') as f:
        fieldnames = ['Наименование', 'Адрес', 'Описание', 'Бренд', 'Сезон', 'Цена', 'Наличие']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';', lineterminator='\r')
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow(info)


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    element = soup.find_all('div', class_='object ga')

    for el in element:
        try:
            name = el.find('a', class_='title').text.strip()
        except ValueError:
            name = ''

        try:
            url = el.find('a', class_='title').get('href').strip()
        except ValueError:
            url = ''

        try:
            description = el.find('span', class_='description').text.strip()
        except ValueError:
            description = ''

        try:
            brand = el.find('span', class_='brand').text.strip()
        except ValueError:
            brand = ''

        try:
            season = el.find('span', class_='collection').text.strip()
        except ValueError:
            season = ''

        try:
            price = el.find('span', class_='price').text.strip()
        except ValueError:
            price = ''

        try:
            available = el.find('span', class_='available').find('span', class_='label').get_text()[:9] + ' ' + el.find(
                'span', class_='available').find('span', class_='label').get_text()[10:]
        except ValueError:
            available = ''

        info = {
            'Наименование': name,
            'Адрес': url,
            'Описание': description,
            'Бренд': brand,
            'Сезон': season,
            'Цена': price,
            'Наличие': available
        }

        write_csv(info)


def main():
    for i in range(1, 9):
        url = f'https://trial-sport.ru/gds.php?s=51525&c1=1070639&c2=1071542&gpp=20&pg={i}/'
        get_data(get_html(url))


if __name__ == '__main__':
    main()
