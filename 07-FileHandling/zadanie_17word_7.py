file=open("linijek30.txt",'r',encoding='UTF-8')
copylines = open("copylines.txt",'a',encoding='UTF-8')

for i in file:
    copylines.write(i)

file.close()
copylines.close()