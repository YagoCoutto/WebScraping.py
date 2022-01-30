# WebScraping.py 🌱🤖

- Estudos sobre Raspagem de dados em sites com tratamento de BOT.
- O software entra no site através da urlopen.
- Usamos a urlopen sobre o objeto REQ, em seguida criamos um objeto através do BEAUTIFULSOUP.
- Localizamos todas tag "A" onde o HREF contenha categorias.
- Ao tentar executar o URLOPEN em algumas paginas você ira se deparar com o erro HTTP Error 403: Forbideen, porque alguns sites tratam robo(scraping) e nao permitem sua execução.
Para burlar essa situação e analisar o serviço do site, foi criado uma requisição passando um HEADERS indicando um USER-AGENT como por exemplo o Chrome/97.0.4692.99.
 
