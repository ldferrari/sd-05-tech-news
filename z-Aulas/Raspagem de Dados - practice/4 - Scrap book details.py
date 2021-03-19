import requests
from parsel import Selector

response = requests.get(
    "http://books.toscrape.com/catalogue/the-grand-design_405/index.html"
)


# Exercício 4 Baseados em uma página contendo detalhes sobre um livro http://books.toscrape.com/catalogue/the-grand-design_405/index.html , faça a extração dos campos título, preço, descrição e url contendo a imagem de capa do livro.
# O preço deve vir somente valores numéricos e ponto. Ex: Â£13.76 -> 13.76 .
# A descrição de ter o sufixo "more..." removido quando existir.
# Os campos extraídos devem ser apresentados separados por vírgula. Ex: título,preço,descrição,capa.
selector = Selector(text=response.text)

# for product in selector.css(".product_main"):
title = selector.css(".product_main").xpath("//title/text()").get()
price = selector.css(".product_main > .price_color::text").re_first(r"\d*\.\d{2}")

img_url = selector.css(".carousel-inner img::attr(src)").get()

description = selector.css("#product_description ~ p::text").get()

availability = selector.css(".product_main .availability::text").re_first("\d")

suffix = "...more"
if description.endswith(suffix):
    description = description[: -len(suffix)]

print(title, price, description, img_url, availability,  sep=', \n')