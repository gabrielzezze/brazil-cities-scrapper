import requests
import json
import os
import pandas as pd
import sys
from scrappers.google_images_scrapper import GoogleImagesScrapper
from scrappers.wikipedia_table_scrapper import WikipediaTablesScrapper
from utilities.file import generate_file_name

DRIVER_PATH='../drivers/chromedriver'
RAW_IMAGES_PATH='../raw_images'

def download_images_from_wikipedia_table_cities():
    wikipedia_scrapper = WikipediaTablesScrapper()
    brazil_cities_table = wikipedia_scrapper(url='https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_acima_de_cem_mil_habitantes')[0]

    google_images_scrapper = GoogleImagesScrapper(DRIVER_PATH, RAW_IMAGES_PATH)
    if brazil_cities_table is None:
        return 'error'
    
    for city_data in brazil_cities_table:
        uf = city_data.get('Unidade federativa', None)
        city = city_data.get('Município', None)

        if uf is None or city is None:
            return 'error'

        file_name = generate_file_name(uf, city, 'jpg')
        google_images_scrapper(f'{city} {uf}', file_name)


def download_images_from_ibge_excel():
    columns = ['UF', 'Município']
    
    cities_df = pd.read_excel('../data/ibge_brazil_cities.xlsx')
    filtered_cities = cities_df[columns]

    uf_list = filtered_cities[columns[0]].tolist()
    cities_list = filtered_cities[columns[1]].tolist()

    google_images_scrapper = GoogleImagesScrapper(DRIVER_PATH, RAW_IMAGES_PATH)
    for i in range(len(cities_list)):
        uf = uf_list[i]
        city = cities_list[i]

        if uf is None or city is None:
            return 'error'

        file_name = generate_file_name(uf, city, 'jpg')
        google_images_scrapper(f'{city} {uf}', file_name)



if __name__ == "__main__":
    args = sys.argv
    if '--ibge' in args:
        print('Using IBGE excel data')
        download_images_from_ibge_excel()

    elif '--wikipedia' in args:
        print('Using wikipedia table data')    
        download_images_from_wikipedia_table_cities()
    
    else:
        print('No valid args provided')