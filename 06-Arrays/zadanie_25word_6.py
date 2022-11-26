def occurs(number, array):
    for i in array:
        if i == number:
            return True
        else:
            continue
    return False
n=int(input("Wybierz liczbę: "))
print(occurs(n,[15, 38, 7, 23, 14]))