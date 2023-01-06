import statistics
class statistic:
    def __init__(self):
        self.array = [12, 37, 6, 9, 17]
        self.displayy=""
        self.greatest=0
        self.smallest=self.array[0]
        self.arithmetic_number=0
        self.sum = 0
        self.median =0

    def add(self,number):
        self.array.append(number)
    def display(self):
        for i in self.array:
            self.displayy=self.displayy + str(i)+', '
    def the_greatest(self):
        for i in self.array:
            if i>self.greatest:
                self.gratest=i
    def the_smallest(self):
        for i in self.array:
            if i<self.smallest:
              self.smallest=i
    def arithmetic(self):
        for i in self.array:
            self.sum += i
        self.arithmetic_number = self.sum / len(self.array)
    def mediana(self):
        self.median = statistics.median(self.array)
    def show(self):
        print(f"twoja lista: {self.displayy[:-2]}\nnajwiększa liczba: {self.gratest}\nnajmniejsza liczba: {self.smallest}\nśrednia arytmetyczna liczb: {round(self.arithmetic_number,2)}\nmediana: {self.median}")



test=statistic()
test.add(56)
test.display()
test.the_greatest()
test.the_smallest()
test.arithmetic()
test.mediana()
test.show()