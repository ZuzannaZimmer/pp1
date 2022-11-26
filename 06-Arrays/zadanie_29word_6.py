a=[1,3,2,4,5,7,6]

n=float(input("Wybierz liczbę: "))
count=0
for i in a:
    if i>n:
        count=count+1
print(count)