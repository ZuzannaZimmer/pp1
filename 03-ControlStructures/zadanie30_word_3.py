liczba = int(input ("Enter number: "))  
  
print (f"Prime numbers:", end=' ')  
for number in range (1, liczba + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number,end=' ') 