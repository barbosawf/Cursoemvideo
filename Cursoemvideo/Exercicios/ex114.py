"""
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""


import requests
import urllib
import urllib.request

try:
    response = requests.get('http://www.pudim.com.br/')
    if response.status_code == 200:
        print('\33[0;33mSite acessado com sucesso!\33[m')
except requests.exceptions.ConnectionError:
    print('\33[0;31mUm erro de conexão aconteceu!\33[m')
print()
try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print('\33[0;31mUm erro de conexão aconteceu!\33[m')
else:
    print('\33[0;33mSite acessado com sucesso!\33[m')
    print(site.read())  # apresenta o conteúdo html que está dentro do site.
