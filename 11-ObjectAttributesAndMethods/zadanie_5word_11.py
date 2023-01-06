class Music():

    def __init__(self,artist,track,album,year):
        self.artist = artist
        self.track = track
        self.album = album
        self.year = year    

    def __str__(self):
        return f"Performer:{self.artist} \nSong: {self.track}\nAlbum: {self.album}/nYear: {self.year}" 


m=Music("Ed Sheeran","Hearts","Divide",2017)
print(m)