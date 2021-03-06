from bs4 import BeautifulSoup

def MetaText(html):
    
    soup = BeautifulSoup(html.text,'html.parser')

    # title in meta      
    meta = [title.text for title in soup.find_all('title')]

    # description in meta
    des = soup.find('meta', attrs={'name':'description'})
    if 'content' in str(des):
        des = descripcion.get('content')
        meta.append(des)
    
    # keywords in meta
    keywords = soup.find('meta', attrs={'name':'keywords'})
    if 'content' in str(keywords):
        keywords = keywords.get('content')
        meta.append(keywords)
    
    # 
    meta = [item.lower() for item in meta]

    return meta
