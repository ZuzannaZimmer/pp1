# class Students():
#     id = 100000
#     def __init__(self,name,surname,field):
#         self.name = name
#         self.surname = surname
#         self.field = field
    

#     def __str__(self):
#         return f"{self.name} {self.surname} ({Students.id}) {self.field}"

# m = Students("Jan", "Nowak", "Informatyka")
# print(m)

# Students.id += 1

# n=Students("Paweł", "Kowalski", "Informatyka")
# print(n)

# Students.id += 1

# k=Students("Kamila", "Maj", "Zarzadzanie")
# print(k)




class Students():
    id = 100000
    def __init__(self,name,surname,field):
        self.name = name
        self.surname = surname
        self.field = field
        self.id = id
        Students.id+=1
    

    def __str__(self):
        return f"{self.name} {self.surname} ({Students.id}) {self.field}"

m = Students("Jan", "Nowak", "Informatyka")
print(m)

n=Students("Paweł", "Kowalski", "Informatyka")
print(n)

k=Students("Kamila", "Maj", "Zarzadzanie")
print(k)