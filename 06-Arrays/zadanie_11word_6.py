m = ['styczen','luty','marzec','kwiecien','maj','czerwiec','lipiec','sierpien','wrzesien','pazdziernik','listopad','grudzien']

def month(n):
    return m[n-1]

print(month(1))
print(month(2))
print(month(11))
print(month(12))