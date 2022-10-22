wpsa = float(input("Wpisz wiek psa: "))
if wpsa <= 2:
    wlud = wpsa * 10.5 
    print(f"Wiek psa w przeliczeniu na ludzkie lata wynosi: {wlud}")
elif wpsa > 2:
    wlud= (wpsa - 2) * 4 + 21
    print(f"Wiek psa w przeliczeniu na ludzkie lata wynosi: {wlud}")