import json

students=open("students.json","r")
data = json.load(students)

limited=open("limited.json",'a')
limited.write("[")
x=0
while x<len(data):
    limited.write('{') 
    for key,value in data[x].items():
        if key == "name" or key == "surname": 
            limited.write('"'+key+'"'+":"+'"'+value+'"'+','+'\n')
        if key == "student_id":
            limited.write('"'+key+'"'+":"+str(value))
        x=x+1
    limited.write('}'+','+'\n')
limited.write("]")

limited.close()
students.close()