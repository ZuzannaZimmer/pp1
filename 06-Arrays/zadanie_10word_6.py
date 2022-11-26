arr = [1,2,3,4,5,6,7,8,9]
x=0
i=0
countp = 0
countnp = 0
while len(arr)>x:

    if arr[i]%2 == 0:
        countp=countp+1
    if arr[i]%2 != 0:
        countnp=countnp+1
    x=x+1
    i=i+1
print("odd:",countnp,"even:",countp)
    