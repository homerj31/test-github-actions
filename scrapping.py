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

      # Extraer todos los
      #  titulos = [titulo.string for titulo in soup.find_all('h1')]
      # print(titulos)

      # Extraer todos los enlaces <a>
        enlaces = [urljoin(url, enlace.get('href')) for enlace in soup.find_all('a')]

        for enlance in enlaces:
            print (enlance)
        # og_image = soup.find('meta', property='og:image')
        # if og_image:
        #     print(og_image['content'])
        # else:
        #     print('No se encontró la imagen')
            
def html_extract (url: str):

    response = requests.get(url)

    if response.status_code == 200:
        print('La petición fue exitosa')

        html = response.text
        #print(html)            
        # Guardar en un archivo
        with open("pagina.html", "w", encoding="utf-8") as f:
            f.write(html)

scrape_url('http://petiteteenagergalleries.com/galleries')

#html_extract('http://petiteteenagergalleries.com/galleries')
