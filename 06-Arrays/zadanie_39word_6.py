a=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]


x=0
razy=1
while x<len(a):
    liczba=1
    y=0
    for i in a[x]:
        a[x][y]=liczba*razy
        y=y+1
        liczba=liczba+1
    print(a[x])
    x=x+1
    razy=razy+1

    