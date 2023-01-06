class tv:

    def __init__(self):
        self.is_on = False         #zmienna logiczna
        self.channel = 1            #początkowy kanał
        self.channels = []           #pusta lista kanałów
        self.volume = 0

    def turn_on(self):              #włączanie telewizora
        self.is_on=True

    def turn_off(self):             #wyłączanie telewizora
        self.is_on=False

    def set_channel(self,new_channel_no):       #ustawianie numeru kanału
        self.channel = new_channel_no

    def set_channels(self,channels_list):       #ustawianie listy nazw kanałów (wyciąga z listy i dodaje do tablicy)
        for i in channels_list:
            self.channels.append(i)

    def show_channels(self):        #pokazuje liste nazw kanałów
        print(self.channels)
    
    def volume_add(self):           #dodaje głośność o 1
        if self.volume < 10:        #maksymalnie 10
            self.volume += 1

    def volume_sub(self):           #zmniejsza głośność o 1
        if self.volume != 0:        #minimalna głośność 0
            self.volume -= 1        


    def show_status(self):          #pokazuje status kanałów
        if self.is_on == True:      #jeśli telewizor włączony
            if self.channel >= 1 and self.channel <= 7:
                print(f"TV is turned on, channel {self.channel} {self.channels[self.channel-1]}, volume: {self.volume}")
            else:
                print(f"TV is turned on, channel {self.channel}, volume: {self.volume}")
        else:
            print("Tv is turned off")

telewizor=tv()                                                                          #ustawić zmienną
telewizor.set_channels(("TVP1","TVP2","Polsat","TVN","Filmbox","Discovery"))            #po funkcji dać nawiasy   
telewizor.turn_on()
telewizor.set_channel(5)
telewizor.show_status()
telewizor.show_channels()
telewizor.set_channel(1)
telewizor.show_status()
telewizor.volume_add()
for i in range(11):             #dodaje żeby sprawdzić czy jest do 10
    telewizor.volume_add()
telewizor.show_status()
telewizor.volume_sub()
telewizor.volume_sub()
telewizor.show_status()
telewizor.turn_off()
telewizor.show_status()