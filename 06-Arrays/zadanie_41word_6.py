a=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
print(a)


x=0
while x<len(a):
    o=a[x][0]
    a[x][0]=a[x][-1]
    a[x][-1]=o
    x=x+1
print(a)
