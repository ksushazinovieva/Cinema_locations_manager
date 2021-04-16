from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import urlparse
import json


def process(url_):
    bs_obj = bs(urlopen(url_), 'html.parser')
    dict = {'description': '', 'photo': ''}
    dict['link'] = url_
    dict['description'] += bs_obj.find('div', class_="name col-left").find('h2').get_text() + ", категории: "
    description = bs_obj.find_all('div', class_='row')
    i = 0
    for elem in description:
        if (i != 0) :
            dict['description'] += ' ' + elem.find_all('a')[1].get_text()
        else:
            dict['description'] += elem.find_all('a')[1].get_text()
        i += 1
    pager = bs_obj.find('div', class_='pager')
    i = 0
    for elem in pager.find_all('a'):
        if elem.find('img') and (i < 10):
            photo_link = elem.find('img').get('src')
            dict['photo'] += ' http://locationhunters.ru' + str(photo_link)
    return dict

list = []

for i in range(2295, 300, -1):
    url_new = 'https://locationhunters.ru/new_catalog/detail.php?ID=' + str(i)
    bs_obj = bs(urlopen(url_new), 'html.parser')
    if not (bs_obj.find('font', class_='errortext')):
        dict = process(url_new)
        dict['price'] = 'По запросу у владельца'
        list.append(dict)
        with open('data_location_hunters4.json', 'w') as f:
            json.dump(list, f)

