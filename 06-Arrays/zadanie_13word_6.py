a=[[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
parzyste=0
nieparzyste=0

x=0
while x<len(a):
    for i in a[x]:
       if i%2==0:
        parzyste+=i
    x=x+1

print(parzyste)
