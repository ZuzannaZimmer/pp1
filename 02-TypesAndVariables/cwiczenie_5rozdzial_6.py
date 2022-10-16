text = 'X-DSPAM-Confidence: 0.8475'
spacja = text.find(' ')
ostatni = text.find('5')
ciag = float(text[spacja+1:ostatni+1])
print(ciag)