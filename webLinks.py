from bs4 import BeautifulSoup
from urllib.parse import urlparse
from pandas.core.common import flatten

def CleanLinks(link_list):
    '''takes a list of items, compares them to a list of file extensions, and removes those where it matches'''
    
    doc_extensions = ['.txt', '.doc', '.docs', '.odt','.pdf', '.csv', '.xls', '.xlsx',
                      '.jpg', '.jpeg','.png','.bmp', '.gif', '.tif', '.img', 
                      '.avi', '.mp3', '.mp4', '.mwv', '.wav', '.wma',
                      '.exe', '.bat', '.dll', '.sys','.zip', '.rar', '.tar', '.iso',
                      '.api','.woff2','.js','.css', '.inp', '.lrgw']
    
    # from last to first 
    for link in reversed(link_list):      
        for ext in doc_extensions:           
            if ext in link:
                link_list.remove(link)
                break
                
    return link_list


def WebLinks(url, html):
    '''receives a request and goes through it to return the links it contains'''
    
    soup = BeautifulSoup(html.content, 'html.parser')
    
    # all links
    href = [tag.get('href') for tag in soup.find_all(href=True)]
    
    # if they start in http they are urls
    urls = [link for link in href if link[:4] == 'http']
    
    # if they do not start with http they are path
    paths = [link for link in href if urlparse(link).path != '' and urlparse(link).netloc =='']
    
    paths = [url + path for path in paths]

    # we join the two lists
    urls += paths
    
    urls = [url.split() for url in urls]  # we avoid having two links in a row
    urls = list(flatten(urls))            # flatten the list
    urls = sorted(set(urls))              # order, eliminate duplicates
    
    # finaly clean docs
    urls = CleanLinks(urls)

    return urls
