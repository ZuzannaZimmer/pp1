film_titles = ['menu','Do ostatniej kości','Osobliwość','Black Adam']
file = open('filmy.txt','x', encoding='UTF-8')
z=''
for line in film_titles:
    file.write(line)
    file.write('\n')
file=open('filmy.txt','r')
file_content = file.read()
print(file_content)
file.close()