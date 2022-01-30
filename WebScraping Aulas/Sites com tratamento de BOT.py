from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

req = Request("https://www.tudogostoso.com.br", headers={'User-Agent': 'Chrome/97.0.4692.99'})
html = urlopen(req).read()

soup = BeautifulSoup(html, "html.parser")

links = soup.findAll("a",  {"href":re.compile("/categorias/")})

for link in links:
    print(link["href"])