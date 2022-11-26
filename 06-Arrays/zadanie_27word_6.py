a=[5,1,9,6,1]

x=0
najwieksza=0
for i in a:
    if x<a[najwieksza]:
        x=a[najwieksza]
    najwieksza=najwieksza+1


y=x
najmniejsza=0
for i in a:
    if y>a[najmniejsza]:
        y=a[najmniejsza]
    najmniejsza=najmniejsza+1

print(x-y)