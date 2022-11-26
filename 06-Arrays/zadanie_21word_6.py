def compare(array1, array2):
    x=0
    if len(array1)==len(array2):
        for i in range(len(array2)):
            if array1[x]==array2[x]:
             x=x+1
            else:
                return False
        return True
    else:
        return False

print(compare([5,3,1],[5,3,1]))
