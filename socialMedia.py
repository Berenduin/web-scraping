import webLinks from WebLinks


def RRSSLinks(url, html):
    '''receives a list of links and returns which are social networks'''
    
    links = WebLinks(url, html)
    
    # rrss
    RRSS = ['www.instagram', 'facebook', 'twitter', 'tiktok',
            'www.pinterest', 'snapchat', 'linkedin', 'youtube',
            'whatsapp', 'telegram', 'messenger']
    
    social_media = [link for link in links for RS in RRSS if RS in link]
    
    # remove posts
    publi = ['/p/', '/video/', '/photo/','/status/', '/watch', '/pin/', '/stories/', '/videos/']
    
    social_media = [media for media in social_media for pub in publi if pub not in media]
    
    social_media = sorted(set(social_media))
    
    return social_media
