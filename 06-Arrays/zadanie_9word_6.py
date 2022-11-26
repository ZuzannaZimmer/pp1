arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']


longest=len(arr[0])
zmienna=arr[0]

print('names:')
for i in arr:
    print(i, end=' ')
print('')
for i in arr:
    if(len(i)>longest):
        longest=len(i)
        zmienna=i
print('longest name:', zmienna)