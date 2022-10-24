def num():
    N = int(input("Wpisz ilość liczb: "))
    for i in range(1, N+1):
        print(i, end=" ")

num() 

print()

def numm(x):
    for i in range(1,x+1):
        print(i, end=" ")

numm(15)