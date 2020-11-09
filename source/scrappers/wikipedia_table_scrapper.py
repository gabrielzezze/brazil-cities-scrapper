from .index import Scrapper
from bs4 import BeautifulSoup
import urllib

class WikipediaTablesScrapper(Scrapper):
    def __call__(self, url):
        req = urllib.request.urlopen(url)
        raw_response = req.read().decode()

        html = BeautifulSoup(raw_response, 'html.parser')
        tables = html.find_all('table', class_='sortable')

        tables_headings = []
        all_tables = []
        for table in tables:
            table_data = []
            raw_headings = table.find_all('th')
            headings = [head.text.strip() for head in raw_headings]
            tables_headings.append(headings)

            rows = table.find_all('tr')
            for row in rows:
                table_dict = {}
                raw_row_data = row.find_all('td')
                if not raw_row_data:
                    continue
                
                row_data = [data.text.strip() for data in raw_row_data]
                for index in range(len(headings)):
                    table_dict[headings[index]] = row_data[index]

                table_data.append(table_dict)
            all_tables.append(table_data)
        
        return all_tables



