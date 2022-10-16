a = int(input("Podaj wartość bok a: "))
b = int(input("Podaj wartość bok b: "))
c = int(input("Podaj wartość bok c: "))
p = (a+b+c)/2
heron = (p*(p-a)*(p-b)*(p-c))**0.5
print("pole obliczone wzorem herona: ",float(heron)) 