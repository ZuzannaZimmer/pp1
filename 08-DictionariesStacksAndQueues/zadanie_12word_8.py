import json

x={"nazwa":"StarWars",
"rok":1977,
"aktor":"Harrison Ford",
"czesc":1,
"rezyser":"Gorge Lucas"
}

f=open("film.json","a")

json.dump(x,f,indent=4)

f.close()