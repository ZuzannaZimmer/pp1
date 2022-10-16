godziny = input("podaj liczbę godzin\n")
stawka = input("podaj stawkę godzinową\n")
wynagrodzenie = float(godziny) * float(stawka)
if float(godziny) > 40 :
   x = float(godziny) % 40
   godziny = 40 * float(stawka) + x * float(stawka) * 1.5
   wynagrodzenie = float(godziny)
   print("wynagrodzenie:", wynagrodzenie)
else :
    print("wynagrodzenie:", wynagrodzenie)