arr = [2, 3, 7, 5, 4]

print(arr)
print(len(arr))
print(arr[0])
print(arr[1])
print(arr[4])
print(arr[3])
print(arr[0]+arr[4])
print(arr[2])

for i in arr:
    print(i,end=" ")
print()
for i in range(0, int(len(arr)/2)+1):
    print(arr[i],end=' ')