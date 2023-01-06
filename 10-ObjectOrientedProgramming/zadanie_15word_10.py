import random
class term:
    
    def __init__(self):
        self.temperatura = 0
        self.term_status = False

    def term_on(self):
        self.term_status = True
    def term_off(self):
        self.term_status = False
    def term_measure(self):
        if self.term_status == True:
            self.temperatura = round(random.uniform(34.0,42.0),1)
    def status(self):
        if self.temperatura >=37.0:
            print("gorączka")
        if self.temperatura >= 41.0:
            print("gorączka","krytyczna temperatura")
    def term_display(self):
        print(f"Twoja temperatura: {self.temperatura}C")

tem = term()
tem.term_on()
tem.term_measure()
tem.term_display()
tem.status()
tem.term_off()