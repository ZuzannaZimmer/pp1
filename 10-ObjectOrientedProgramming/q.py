import re
# class TV:
#     def __init__(self):
#         self.is_on=False
#         self.channel=1

    
#     def turn_on(self):
#         self.is_on=True
#     def turn_off(self):
#         self.is_on=False
#     def show_status(self):
#         if self.is_on == True:
#             print(f'TV is on, channel {self.channel}')
#         else:
#             print('Tv is off')
#     def set_channel(self, num):
#         self.channel=num



# telewizor=TV()
# telewizor.show_status()
# telewizor.turn_on()
# telewizor.show_status()
# telewizor.set_channel(5)
# telewizor.show_status()

import random

# Generowanie losowej liczby całkowitej
n = random.randint(100000000000000, 999999999999999)

# Sformatowanie liczby jako ciągu z odstępami co 4 cyfry
formatted_number = '{:11,d}'.format(n)

print(formatted_number)
