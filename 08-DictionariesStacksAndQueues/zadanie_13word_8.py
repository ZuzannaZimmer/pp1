import json

uczen = {
    'imie':"Jakub",
    'nazwisko':"Nowak",
    'klasa':3,
    'pelnoletnosc':True,
    'numer_rodzica':'37892347'
}

f=open("student.json","a")

json.dump(uczen,f,indent=4)

f.close()