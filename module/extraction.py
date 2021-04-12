import requests
import re
from bs4 import BeautifulSoup

from module.product import Product


def get_products_links():

    r = requests.get('https://www.hebe.pl/zapachy-dla-mezczyzn/')
    r_html = r.text

    soup = BeautifulSoup(r_html, 'html.parser')
    perflink = []

    for tag in soup.find_all('a', class_="product-tile-clickable js-product-link"):
        perflink.append("https://www.hebe.pl/zapachy-dla-mezczyzn" + tag["href"])

    return perflink


def get_product_data(link):

    r = requests.get(link)
    print(link)
    r_html = r.text

    soup = BeautifulSoup(r_html, 'html.parser')

    translator = str.maketrans({"\n": None, "\t": None, ".": None})

    try:
        last_t = soup.find('h1', class_="product-content__brand")
        last_c = soup.find(id="product-ingredients").find("div", class_="ui-expandable__inner")
        name = last_t.getText().translate(translator)
        comp = last_c.getText().translate(translator).split(',')
        if len(comp) < 2:
            comp = comp.split('  ')
        perfume = Product(name, comp)
    except:
        return False

    return perfume
