wartosc = input("Wpisz wartość pomiędzy 0.0 a 1.0 :")
try:
    wartosc = float(wartosc)
except:
    print("Niepoprawna wartość")
if float(wartosc) < 0.0 or float(wartosc) > 1.1 :
  print("Niepoprawna wartość:")
if wartosc > 0.0 and wartosc < 1.0 :
  if float(wartosc)>= 0.9 :
    print('5,5')
  else:
   if float(wartosc)>= 0.8 :
    print('4,5')
   else:
    if float(wartosc)>= 0.7 :
     print('4,0')
    else:
     if float(wartosc)>= 0.6 :
      print('3,5')
     else:
      if float(wartosc)>= 0.5 :
        print('3,0')
      else:
       if float(wartosc)< 0.5 :
        print("2") 