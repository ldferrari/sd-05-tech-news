import requests
from parsel import Selector
from time import sleep


URL = 'https://www.tecmundo.com.br/novidades'


def fetch_content(url=URL, timeout=3, delay=0.5, page=1):
    try:
        response = requests.get(f'{url}?page={page}', timeout=timeout)
        if (response.status_code != 200):
            return ''
        sleep(delay)
        return response.text
    except OSError:
        print('Deu algum erro')
        return ''


def scrape(fetcher, pages=1):
    main_list = []
    for x in range(1, pages+1):
        resp = fetcher(page=x)
        selector = Selector(text=resp)
        h3 = 'h3[class=tec--card__title]'
        classe = 'a.tec--card__title__link::attr(href)'
        trash_list = selector.css(f'{h3} {classe}').extract()
        print(len(trash_list))
        for x in trash_list:
            response = fetcher(url=x)
            selector2 = Selector(text=response)
            title = "h1.tec--article__header__title::text"
            timestamp = "div.tec--timestamp__item time::attr(datetime)"
            writer_selector = "a.tec--author__info__link::text"
            writer = selector2.css(writer_selector).getall()
            if len(writer) > 0:
                writer = writer[0].strip()
            else:
                writer = 'Sem autor'
            shares_count = "div.tec--toolbar__item::text"
            shares_count = selector2.css(shares_count).getall()
            if len(shares_count) > 0:
                shares_count = shares_count[1].strip()
                if (len(shares_count) == 0):
                    shares_count = 0
                else:
                    shares_count = shares_count[0]
            else:
                shares_count = 0
            comments = "button.tec--btn::attr(data-count)"
            comments = selector2.css(comments).getall()
            if len(comments) > 0:
                comments = comments[0]
            else:
                comments = 0
            summary = "div.tec--article__body p"
            summary = selector2.css(summary).getall()
            summary = summary[0].strip()
            sources = "div.z--mb-16 div"
            sources = selector2.css(sources).getall()
            print(type(sources[0]))
            dados = {
                "url": x,
                "title": selector2.css(title)[0].extract().strip(),
                "timestamp": selector2.css(timestamp)[0].extract(),
                "writer": writer,
                "shares_count": shares_count,
                "comments_count": comments,
                "summary": summary
            }
            main_list.append(dados)
            # print(x)
            # print(len(main_list))
        """n = 0
        for x in lista:
            print(lista[n])
            print('\n')
            n += 1
            sleep(2)
        """
    print(main_list)
    return main_list


scrape(fetcher=fetch_content, pages=1)
