import random
class bank:
    
    def __init__(self):
        self.bank_number = 0
        self.saldo = 0.00
    def create(self):
        self.bank_number = random.randint(10000000000000000000000000,99999999999999999999999999)
        # self.bank_number= '{:2} {:4} {:4} {:4} {:4} {:4} {:4}'.format(*str(self.bank_number)[:26])
    def add(self,number):
        self.saldo+=number
    def sub(self,number):
        if number>self.saldo:
            print("Niewystarczające środki na koncie")
        if number<=self.saldo:
            self.saldo-=number
            print(f"Wypłaciłeś {number} zł")
    def status(self):
        print(f"Numer konta: {self.bank_number}\nSaldo: {self.saldo}")

test = bank()
test.create()
test.status()
test.add(400)
test.status()
test.sub(300)
test.status()
test.sub(300)
test.status()

