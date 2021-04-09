import requests
import re

from bs4 import BeautifulSoup


def get_products_links():
    r = requests.get('https://www.hebe.pl/zapachy-dla-mezczyzn/?start=0&sz=300')
    r_html = r.text

    soup = BeautifulSoup(r_html, 'html.parser')
    perflink = []

    for tag in soup.find_all('a', class_="product-tile-clickable js-product-link"):
        perflink.append("https://www.hebe.pl/zapachy-dla-mezczyzn" + tag["href"])

    return perflink


def get_product_data():
    perflink = get_products_links()
    perf_data = []

    for each in perflink:
        r = requests.get(each)
        print(each)
        r_html = r.text

        soup = BeautifulSoup(r_html, 'html.parser')

        if soup.find(string=re.compile("Składniki")) == None:
            continue

        last_t = soup.find('span', class_="pdp-name")

        last_c = None
        for tagC in soup.find_all('div', class_="section-body"):
            for anchorC in tagC.find_all("p"):
                last_c = anchorC

        try:
            perfdict = {"name": last_t.getText().strip(" \n.").split(','),
                        "comp": last_c.getText().strip(" \n.").split(',')}
            if len(perfdict["comp"]) < 2:
                perfdict["comp"] = perfdict["comp"][0].split('\n')
            perf_data.append(perfdict)
        except:
            continue

    return perf_data