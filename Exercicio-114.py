import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://pudim.com')

except urllib.error.URLError:
    print('O site não esta acessivel')


else:
    print('Tudo ok!')