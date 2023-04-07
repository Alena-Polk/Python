import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    res = requests.get(url)
    return res.text


def write_csv(data):
    with open('offelia_products.csv', 'a', newline='') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\r')
        writer.writerow((data['name'], data['availability'].strip(), data['price'].strip()))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    p1 = soup.find('div', class_='col-lg-9')
    products = p1.find_all('div', class_='product_show')

    for product in products:
        name = product.find_all('p', class_='product_show_content_block_text')[0].find('a').text
        availability = product.find_all('p', class_='product_show_content_block_text')[3].find('strong').text + product.find_all('p', class_='product_show_content_block_text')[3].get_text()[11:]
        price = product.find_all('p', class_='product_show_content_block_text')[1].find('strong').text + product.find_all('p', class_='product_show_content_block_text')[1].get_text()[11:]
        data = {'name': name, "availability": availability, "price": price}
        write_csv(data)


def main():
    url = 'http://offelia.ru/categories/4'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
