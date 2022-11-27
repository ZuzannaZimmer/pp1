shop=open('shoppinglist.txt','a')  
fish=open('MeatAndFish.txt','r')   
bread=open('GrainsAndBread.txt','r')  

list1=fish.read()
list2=bread.read()
shop.write(list1)
shop.write(list2)

shop.close(),fish.close(),bread.close()