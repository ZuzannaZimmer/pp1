import stack

number = int(input("Wpisz liczbę: "))
count=0

while number>0:
    if number%2==0:
        stack.push(0)
        number=round(number/2)
        count+=1
    else:
        stack.push(1)
        number=round(number/2)
        count+=1

for i in range(count):
    print(stack.pop(),end='')