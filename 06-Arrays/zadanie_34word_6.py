a=[6,8,32,7]
b=[5,3,6,8,56,32,7]
x=0
for i in a:
    x=x+1
    if x!=len(a) and i in b:
        continue
    elif i not in b:
        print(False)
        break
    elif x==len(a) and i in b: 
        print(True)
        break