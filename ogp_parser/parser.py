from bs4 import BeautifulSoup
import requests

def __parse_ogp(metas):
    ogps = list(filter(lambda x: x.has_attr('property'), metas))
    results = {}
    for ogp in ogps:
        prop = str(ogp['property'])
        content = str(ogp['content'])
        if prop not in results:
            results[prop] = []
        results[prop].append(content)
    return results


def __parse_seo(metas):
    ogps = list(filter(lambda x: x.has_attr('name'), metas))
    results = {}
    for ogp in ogps:
        prop = str(ogp['name'])
        content = str(ogp['content'])
        if prop not in results:
            results[prop] = []
        results[prop].append(content)
    return results

def parsedom(dom):
    """
    Get Opengraph data or SEO data.

    Arguments:
        url: target URL
    
    Return:
        [dict] OpenGraph and SEO data
    """
    metas = dom.select('meta');
    metas = list(filter(lambda x: x.has_attr('content'), metas))

    title = str(dom.find('head').find('title').string);
        
    return {
        'title': title,
        'ogp': __parse_ogp(metas),
        'seo': __parse_seo(metas)
    }

def request(url):
    pass
