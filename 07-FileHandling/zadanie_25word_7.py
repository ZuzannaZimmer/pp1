import re

tekst='To be, or not to be, that is the question'
samogloski = re.split("\s", tekst)
print(len(samogloski))