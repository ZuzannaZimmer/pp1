def sum(zdanie):
    count=0
    for i in zdanie:
        if i == 'e':
            count+=1
        else:
            continue
    return count


print(sum('You never get a second chance to make a first impression'))
