arr = [1, 2, 3, 4, 5]

arr[0] = arr[0]-1
arr[4] = arr[4]+4
arr[2] = arr[2]*2
for i in arr:
    i= i+3
    print(i)

# albo
for i in range(0,len(arr)):
    arr[i]=arr[i]+3