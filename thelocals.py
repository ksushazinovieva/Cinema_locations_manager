from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import urlparse
import json

start = urlopen("https://thelocals.ru/snyat-kvartiry-moskva")
soup_start = bs(start, 'html.parser')
list = []
for elem in soup_start.find_all('span', class_='metro__text'):
    station_url = elem.find('a').get('href')
    string_url = urlparse(station_url).path
    new_url = urlopen(elem.find('a').get('href'))
    soup = bs(new_url, 'html.parser')
    for element in soup.find_all('div', class_='OfferCard'):
        dict = {'описание': '', 'фото': []}
        rooms_num = element.find('span', class_='OfferCard__optionsItem').text.strip()
        if (rooms_num[0] == '2' or rooms_num[0] == '3'):
            dict['ссылка'] = 'https://thelocals.ru' + element.find('a', class_='OfferCard__link').get('href')
            for i in element.find_all('span', class_='OfferCard__optionsItem'):
                dict['описание'] += i.text
                dict['описание'] += ' '
            new_url = urlopen(dict['ссылка'])
            new_soup = bs(new_url, 'html.parser')
            for elem in new_soup.find_all('img', class_='OfferGallery__imageImg'):
                dict['фото'].append(elem.get('src'))
            dict['цена аренды в месяц'] = element.find('span', class_='OfferCard__priceValue').text.strip()
            list.append(dict)
with open('data.json', 'w') as f:
    json.dump(list, f)



