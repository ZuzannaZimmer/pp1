f=open('linijek30.txt','r',encoding='UTF-8')


x=0
five=5

for i in f:
    print(i,end='')
    x=x+1
    if x==five:
        five=five+5
        if five!=35:
            nakliknij=input('')
        