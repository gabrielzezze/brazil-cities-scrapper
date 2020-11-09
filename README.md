# Brazil Cities Scrapper
### Gabriel Zezze
### 2020

## 🇧🇷
Projeto de scraping de cidades do Brasil e download de imagens destas. Existem duas fontes de dados das cidades do Brasil usadas neste projeto, uma delas sendo um excel do ibge sobre todas as cidades do Brasil e a outra uma tabela do wikipedia com todas as cidades do  Brasil que possuem mais de cem mil habitantes.
No caso de usar a primeira fonte de dados (excel do IBGE), os dados são retirados do arquivo através da biblioteca pandas.
No caso de usar a segunda fonte de dados, os dados sao retirados da página do wikipedia através de um processo de scrapping usando BeautifulSoup.
Após a obtenção dos nomes das cidades e unidades federativas, é usado um scrapper feito em selenium para baixar a imagens desta cidade do google imagens.

### Uso:

Dados do wikipedia:
```
pipenv install
pipenv shell
python3 source/main.py --wikipedia
```

Dados do excel do IBGE:
```
pipenv install
pipenv shell
pytho3 source/main.py --ibge
```
<br></br>
## 🇺🇸
Scraping project of cities in Brazil and download of these images. There are two sources of data for Brazil cities used in this project, one of them being an IBGE excel table of all cities in Brazil and the other is a wikipedia table with all cities in Brazil that have more than one hundred thousand inhabitants.
In the case of using the first data source (excel from IBGE), the data are extracted from the file through the pandas library.
In the case of using the second data source, the data is extracted from the wikipedia page through a scrapping process using BeautifulSoup.
After obtaining the names of cities and federative units, a scrapper made in selenium is used to download images of the cities from google images.

### Usage:

Wikipedia data:
```
pipenv install
pipenv shell
python3 source/main.py --wikipedia
```

Excel IBGE data:
```
pipenv install
pipenv shell
pytho3 source/main.py --ibge
```