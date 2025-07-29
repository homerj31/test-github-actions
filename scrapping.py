from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

def scrape_url(url: str):
    headers = {
      'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/131.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print('La petición fue exitosa')

        soup = BeautifulSoup(response.text, 'html.parser')

      # Extraer todos los enlaces <a>
        enlaces = [urljoin(url, enlace.get('href')) for enlace in soup.find_all('a')]

        with open("enlaces.txt", "w", encoding="utf-8") as f:
          
            for enlace in enlaces:
                f.write(enlace + "\n")

def html_extract (url: str):
    response = requests.get(url)
    if response.status_code == 200:
        print('La peticion fue exitosa')
        html = response.text
        # Guardar en un archivo
        with open("pagina.html", "w", encoding="utf-8") as f:
            f.write(html)            

html_extract('http://petiteteenagergalleries.com/galleries')
scrape_url('http://petiteteenagergalleries.com/galleries')

