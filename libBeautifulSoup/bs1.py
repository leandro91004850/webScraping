from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://192.168.1.50:8081/teste.html")
objeto = BeautifulSoup(html.read(), "html.parser") # analise da page

print(objeto.title)
#print(objeto.h1)
print(objeto.find_all("h1"))# buscando todos os h1