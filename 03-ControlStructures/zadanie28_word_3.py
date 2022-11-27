def fibonacci():
    a=0
    b=1
    for i in range(5):
        print(b)
        a,b= b,a+b
        
fibonacci()

def fib(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return (fib(n-1)+fib(n-2))

print(fib(5))        