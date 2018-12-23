from bs4 import BeautifulSoup
import requests

def parser(url):
    """
    Get Opengraph data or SEO data.

    Arguments:
        url: target URL
    
    Return:
        [dict] OpenGraph and SEO data
    """
    res = requests.get(url)
    dom = BeautifulSoup(res.text)
    