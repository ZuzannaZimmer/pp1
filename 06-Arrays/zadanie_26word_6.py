a=[5,1,9,6,1]

x=0
najwieksza=0
for i in a:
    if x<a[najwieksza]:
        x=a[najwieksza]
    najwieksza=najwieksza+1

for i in a:
    if i == x:
        a.remove(x)

y=0
najwieksza2=0
for i in a:
    if y<a[najwieksza2]:
        y=a[najwieksza2]
    najwieksza2=najwieksza2+1  
print(y)
     

    
