from tech_news.database import find_news


def top_5_news():
    news = find_news()
    for art in news:
        art["total"] = (f'${art["shares_count"]+art["comments_count"]}')
    sorted = news.sort("total", reverse=True)
    limited = sorted[:5]
    resultado = []
    for noticia in limited:
        resultado.append((noticia['title'], noticia['url']))
    return resultado


def top_5_categories():
    """Seu código deve vir aqui"""
