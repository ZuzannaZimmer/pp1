import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
print(temperatures)
suma=0
for i in temperatures:
    suma=suma+int(i)
print(suma//3)
