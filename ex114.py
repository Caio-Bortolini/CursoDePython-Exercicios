import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.usf.edu.br/apps/portal2/login')

except:
    print("O site não esta disponivel no momento")

else:
    print("Consegui acessar!")
    print(site.read())

