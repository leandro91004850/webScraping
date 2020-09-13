from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://192.168.1.50:8081/teste.html")
objeto = BeautifulSoup(html.read(), "html.parser")

for link in objeto.find_all("a"):
    #print(link)
    print(link.get("href"))