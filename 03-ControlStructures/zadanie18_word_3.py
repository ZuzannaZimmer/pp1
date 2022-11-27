while True:
    wartosc = int(input('Wpisz dowolną liczbę pieniędzy w złotówkach (bez groszy): '))
    
    if wartosc ==0:
        print(f'0 monet')
        continue

    if wartosc != 0:
        cal=wartosc//5
        reszta=wartosc%5
        print(f'5zł  {cal}')

    if reszta >1:
        cal_reszta =reszta//2
        reszta2=reszta%2
        print(f'2zł  {cal_reszta}')

    if reszta ==1 or cal_reszta ==1:
        cal_reszta1=1
        print(f'1zł  {cal_reszta1}')
        
