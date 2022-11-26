a = [[True,False],[True,True],[False,False]]
x=0
y=0
while x<len(a):
    for i in a[x]:
        if i == True:
            a[x][y]=False
            y=y+1
        if i == False:
            a[x][y]=True
            y=y+1 
    x=x+1
    y=0       
print(a)