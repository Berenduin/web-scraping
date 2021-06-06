from webLinks import WebLinks
from bs4 import BeautifulSoup

def Combinations(items):
  
    items += [i.replace(" ", "-") for i in items if " " in i]     # blanks by -
    items += [i.replace(" ", "_") for i in items if " " in i]     # blanks by _
    items += [i.replace("-", "_") for i in items if "-" in i]     # - by _
    items += [i.replace("_", "-") for i in items if "_" in i]     # vice versa
    
    items = sorted(set(items))
    
    return items


def aboutUsLink(url,html,language):
    
    links = webLinks(url,html)
    
    dic = {'es': ['sobre nosotros', 'quienes somos', 'sobre '],
           'fr': ['qui sommes nous','a propos de nous', 'propos de nous', 'nous '],
           'it': ['chi siamo', 'siamo '],
           'de': ['über uns', 'uber uns','uber '],
           'pt': ['sobre nos', 'quem somos', 'sobre '],
           'nl': ['over ons','over '],
           'en': ['about us', 'about ','who is', 'who are', 'who '],
           'pl': ['o nas', 'nas '],
           'cs': ['o nás', 'kdo je', 'kdo jsou', 'nás ', 'kdo '],
           'ro': ['despre noi', 'cine este', 'care sunt', 'noi ']}
    
    if language == 'en':
        keywords = dic['en']
    else:
        keywords = dic[language] + dic['en']
    
    # all the possibilities
    keywords = Combinations(keywords)
    
    contact_links = [[link for item in keywords] for link in links if item in link]
    contact_links = sorted(set(contact_links))
    
    return contact_links
