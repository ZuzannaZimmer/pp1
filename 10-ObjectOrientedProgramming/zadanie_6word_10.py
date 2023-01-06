class University():

    # object constructor (__init__ method)
    def __init__(self):
        # object attributes (object features)
        self.name = 'CUE'    

    def set_name(self, name):
        self.name = name
        return self.name

# object methods (object behaviors)
    def print_name(self):  
        print(self.name)

        
University().print_name()
print(University().set_name("MIT"))
