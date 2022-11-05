def calculator(word):
    x=0
    y=0
    while x < len((word)):
        letter= word[x]
        if letter == "e":
           y=y+1
        x=x+1
    print(y)

calculator("You never get a second chance to make a first impression")  
