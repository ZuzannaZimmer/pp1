
def sum(N):
    j=0
    for i in range(1,N+1):
       j=j+i
    return j

print(sum(10))

def suma_r(N):
    if N==0: return 0
    return N+suma_r(N-1)

suma_r(10)