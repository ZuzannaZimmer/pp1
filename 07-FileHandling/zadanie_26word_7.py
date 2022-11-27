import re
tekst=open("tekst.txt",'r')
ttt=tekst.read()
szesc='[a-zA-Z]{6}'
lista=re.findall(szesc,ttt)

