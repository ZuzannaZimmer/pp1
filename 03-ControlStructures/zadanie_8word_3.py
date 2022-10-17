paul = 21
annie = 18

if paul and annie >= 18:
    print("Paul i Annie są dorośli")
elif paul >= 18 and annie < 18:
    print("Paul jest dorosły, a Annie nie")
elif annie >= 18 and paul < 18:
    print("Annie jest dorosły, a Paul nie")
else:
    print("Paul i Annie nie są dorośli")