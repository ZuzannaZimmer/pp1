def month(n):
    x=0
    j = ['styczen','luty', 'marzec', 'kwiecien', 'maj', 'czerwiec','lipiec', 'sierpien', 'wrzesien', 'pazdziernik', 'litopad','grudzien']
    for z in range(1):
        for c in j:
         x=x+1
         if n ==x:
            print(x,c)
         

month(4)