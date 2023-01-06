class phone:
    def __init__(self,name,model,numer):
        self.name=name
        self.model=model
        self.numer=numer
        self.bateria=0
        self.internett=False
    def __str__(self):
        return f'Imię właściciela telefonu: {self.name}, model jego telefonu to {self.model}, a numer telefonu to: {self.numer}, telefon ma {self.bateria}%, internet jest {self.internett}'
    def ladowanie(self,ile):
        self.bateria+=ile
    def internet(self):
        self.internett=True

x=phone('Mark','Samsung',3475893)
x.ladowanie(40)
x.internet()
print(x)
    
