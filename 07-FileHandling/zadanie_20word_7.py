import random
f=open("losowe.txt",'a')

for i in range(1,51):
    f.write(str(random.randint(100,1000))+'\n')

f.close()