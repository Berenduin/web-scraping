import re
from webLinks import CleanLinks


def SacarCorreos(html):
    '''receives an http.get request and searches inside for emails'''
    
    text = html.text
    
    emails = [email for email in re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",text)]
    
    emails = [email.lower() for email in emails] # convertimos la lista en minuscula
    
    # clean docs
    emails = CleanLinks(emails)
    
    # role-based emails
    roles = ['abuse@', 'admin@','billing@','compliance@','devnull@','dns@','ftp@',
             'hostmaster@','inoc@','ispfeedback@','ispsupport@','list-request@',
             'list@','maildaemon@','noc@','no-reply@','noreply@','null@','phish@',
             'phishing@','postmaster@','privacy@','registrar@','root@','security@',
             'spam@','support@','sysadmin@','tech@','undisclosed-recipients@',
             'unsubscribe@','usenet@','uucp@','webmaster@','www@']
    
    # delete emails based on roles
    emails = [[email for email in emails] for rol in roles if rol not in email]
    
    emails = sorted(set(emails))    
    return emails
