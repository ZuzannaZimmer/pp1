import random

def rand_elem(array):
    return array[random.randint(0,len(array)-1)]


print(rand_elem([3,6,8,4,2,7,9,6,44]))