a = [[0,0,0],[0,0,0],[0,0,0]]


x=0
y=0
for i in range(0,len(a)):
    if a[x][y]==0:
        a[x][y]=1
    x=x+1
    y=y+1

print(a)
