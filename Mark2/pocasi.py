from bs4 import BeautifulSoup
import requests


page = requests.get("http://www.meteo-pocasi.cz/maps/cz/zlinsky/1240-meteostanice-uherske-hradiste/")

soup = BeautifulSoup(page.content, 'html.parser')
dalsi = soup.find("div", {"class": "no_main_page"})
#print(dalsi)


vypis = dalsi.findAll('div', {"class": "boxing"})
opis = dalsi.findAll('div', {"class": "box"})
#print(opis)

for op in opis:
    
    if op.find('div', {"class": "svalue"}) is not None:
        print(op.find('div', {"class": "boxheader"}).text)
        print(op.find('div', {"class": "svalue"}).text)
    else:
        print

