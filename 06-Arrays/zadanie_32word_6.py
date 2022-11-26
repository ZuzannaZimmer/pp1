def f(a):
    for i in a[:-1]:
        print(str(i)+",",end='')
    print(a[-1])
f([2,6,4,5,7])