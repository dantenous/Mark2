from bs4 import BeautifulSoup
import requests
import json


page = requests.get(
    "https://www.bazos.cz/search.php?hledat=grafick%C3%A1+karta&rubriky=www&hlokalita=&humkreis=25&cenaod=&cenado=&kitx=ano")

soup = BeautifulSoup(page.content, 'html.parser')
dalsi = soup.find("div", {"class": "sirka"})
# print(dalsi)

odkaz = dalsi.findAll('table')[0]
vnitrni = odkaz.findAll('td')[1]
vypis = vnitrni.findAll('span', {"class": "vypis"})

dataa = []
for vyp in vypis:
    #dataa[i] = {vyp.find('span').text, vyp.find('img').get('src'), vyp.find('span', {"class": "cena"}).text}
    #dataa['odkaz'] = vyp.find('span')('a')
    dataa.append([vyp.find('span').text, vyp.find('img').get(
        'src'), vyp.find('span', {"class": "cena"}).text])
    """print(vyp.find('span').text)
    print(vyp.find('span')('a'))
    print(vyp.find('img').get('src'))
    print(vyp.find('span', {"class": "cena"}).text)
    print"""
json_dict = {'all': [dataa]}

print(json.dumps(json_dict))
with open('data.txt', 'w') as outfile:
    json.dump(json_dict, outfile)


"""
Verze jedna

from selenium import webdriver
from bs4 import BeautifulSoup


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/home/lukaschvostal/chromedriver", chrome_options=options)


driver.get("https://www.bazos.cz/search.php?hledat=grafick%C3%A1+karta&rubriky=www&hlokalita=&humkreis=25&cenaod=&cenado=&kitx=ano")

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')
dalsi = soup.find("div", {"class": "sirka"})
odkaz = dalsi.findAll('table')[0]
vnitrni = odkaz.findAll('td')[1]
vypis = vnitrni.findAll('span', {"class": "vypis"})


for vyp in vypis:
    print(vyp.find('span').text)
    print(vyp.find('span')('a'))
    print(vyp.img)
    print
"""
