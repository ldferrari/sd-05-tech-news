URL_BASE = "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"


print(scrape(fetcher=fetch_content(URL_BASE), pages=2))
