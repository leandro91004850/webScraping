import re

texto = ("esta é uma aula de python. Esta aula é sobre expressões reggulares. ")

padrao = "leandro"
resultado = re.search(padrao, texto)

if resultado:
    print(resultado)
else:
    print('nao encontrado.')