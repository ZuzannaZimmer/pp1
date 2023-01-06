import json

file=open("euro.json",'r')
kurs=json.load(file)

print("effectiveDate","       ","no","       ",'mid')
for key,value in kurs.items():
    print(value,",","       ")
file.close()