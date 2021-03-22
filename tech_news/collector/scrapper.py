def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=timeout)
    except requests.Timeout:
                return ''
    else:
        if(response.status_code != 200):
                return ''
            time.sleeep(delay)
            return response.text

def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
