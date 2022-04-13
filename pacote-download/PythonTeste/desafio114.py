'''from tabulate import tabulate

d = [ ["Mark", 12, 95],
     ["Jay", 11, 88],
     ["Jack", 14, 90]]

print(tabulate(d, headers=["Name", "Age", "Percent"]))'''

import urllib
import urllib.request
try:
     site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
     print('O site pudim.com.br não está acessível pelo computador')
else:
     print('O site pudim.com.br está acessível pelo computador')
     print(site.read())
     