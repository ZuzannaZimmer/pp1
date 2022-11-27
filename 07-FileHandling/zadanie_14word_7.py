nazwa=str(input("Wprowadź nazwę pliku: "))
f=open(nazwa,'r')
count=0
for line in f:
    count=count+1
print(f"Nazwa pliku: {nazwa}\nIlość linijek: {count}")
f.close()
