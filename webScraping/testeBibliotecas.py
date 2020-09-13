import builtwith
import whois

# builtwith.parse('https://crane-technology.herokuapp.com/')

# IDENTFICANDO O PROPRIERTARIO DE UM SITE.
l = whois.whois('globo.com')
print(l)
