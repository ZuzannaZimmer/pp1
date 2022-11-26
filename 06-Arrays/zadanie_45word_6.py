def f(m):
    x=0
    s=[]
    while x<len(m):
        for i in m[x]:
            s.append(i)
        x=x+1
    return s


print(f([[0 ,3, 7 ,5],[9 ,0 ,9 ,1 ,2]]))