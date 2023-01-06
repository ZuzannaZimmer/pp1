import random
class arrays():

    @staticmethod
    def method_name(number_of_array_elements, value_of_array_elements):
        a=[]
        for i in range(number_of_array_elements):
            a.append(value_of_array_elements)
        print(a)
    @staticmethod
    def method_name2(number_of_array_elements, value_from, value_to):
        b=[]
        for i in range(number_of_array_elements):
            b.append(random.randint(value_from,value_to))
        print(b)
    @staticmethod
    def method_name3(array, value_from, value_to):
        c=0
        for i in array:
            if i>=value_from and i<=value_to:
                c+=1
        print(c)
        




arrays.method_name(4,1)
arrays.method_name2(4,3,5)
arrays.method_name3([1,2,3,4,5,6],2,5)
