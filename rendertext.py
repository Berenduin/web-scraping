from bs4 import BeautifulSoup

def VisibleText(html):
   
    sopa = BeautifulSoup(html.text,'html.parser')
    
    visible_text = [item.lower() for item in sopa.stripped_strings] 
    
    return visible_text
