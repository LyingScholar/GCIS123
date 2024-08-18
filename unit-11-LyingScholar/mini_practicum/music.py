class Time:
    __slots__ = ['hours', 'minutes', 'seconds']

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

class Song:
    __slots__ = ['title','recording_artist','duration']

    def __init__(self, title,recording_artist,duration_colons):
        self.title = title
        self.recording_artist = []
        for x in recording_artist.split(","):
            self.recording_artist.append(x.strip())
        numbers = duration_colons.split(':')
        try:
            self.duration = int(numbers[-1])
        except:
            pass
        try:
            self.duration += int(numbers[-2])*60
        except:
            pass
        try:
            self.duration += int(numbers[-3])*3600
        except:
            pass
        
    def print_song(self):
        hours = self.duration//3600
        minutes = (self.duration%3600)//60
        seconds = self.duration % 60
        if minutes <10:
            minutes = "0" + str(minutes)
        if seconds <10:
            seconds = "0" + str(seconds)
        
        print(self.title,"by",end=" ")
        if len(self.recording_artist) > 1:
            for artist in self.recording_artist:
                print(artist + ",", end = " ")
            print("\b\b  ", end ="")
        else:
            print(self.recording_artist[0], end = " ")
        print(hours,":", minutes,":",seconds,sep="")
        
class Album:
    __slots__ = ['album_title', 'artist_s', 'songs', 'list_of_tracks', 'total_duration_secs']

    def __init__(self,album_title):
        self.album_title = album_title
        self.artist_s = set()
        self.songs = []
        self.list_of_tracks = []
        self.total_duration_secs = 0
        
    def add_song(self, song):
        self.list_of_tracks.append(song.title)
        self.songs.append(song)
        for artist in song.recording_artist:
            self.artist_s.add(artist)
        self.total_duration_secs += song.duration

    def add_songs(self, songs):
        for songie in songs:
            self.add_song(songie)

    def print_album(self):
        print(self.album_title)
        for i in self.songs:
            print("\t",end = "")
            i.print_song()
        print("\nArtists:")
        for i in self.artist_s:
            print("\t",i)
        hours = self.total_duration_secs//3600
        minutes = (self.total_duration_secs%3600)//60
        seconds = self.total_duration_secs % 60
        if minutes <10:
            minutes = "0" + str(minutes)
        if seconds <10:
            seconds = "0" + str(seconds)
    
        print("Total Duration: ",hours,":", minutes,":",seconds,sep="")
    
def get_time(time):
    return '{}:{:02}:{:02}'.format(time.hours, time.minutes, time.seconds)

def main():
    Lunch_break = Album("Lunch Break")
    song1 =Song("11k","Seedhe Maut","2:54")
    song2 =Song("Sick&Proper","Seedhe Maut","2:07")
    song3 =Song("Brand New","Seedhe Maut","2:19")
    song4 =Song("Peace of Mind","Seedhe Maut, Lil Bhavi, Bhaskar, Ab 17","3:56")
    song5 =Song("Pushpak Vimaan","Seedhe Maut, Sonnyjim","3:12")
    song6 =Song("Dikkat","Seedhe Maut, Hurricane","2:37")
    song7 =Song("Kya Challa","Seedhe Maut","1:41")
    song8 =Song("Fanne Khan","Seedhe Maut, yungsta","4:02")
    song9 =Song("First Place","Seedhe Maut","1:58")
    song10 =Song("Champions","Seedhe Maut, Rawal","3:33")
    song11 =Song("Baat Aisi Ghar Jaisi","Seedhe Maut","3:00")
    song12 =Song("Naam Kaam Sheher","Seedhe Maut, Qaab, Rebel 7","2:46")
    
    
    
    song1.print_song()
    
    Lunch_break.add_songs([song1,song2,song3,song4,song5,song6,song7,song8,song9,song10,song11,song12])
    Lunch_break.print_album()
    
    

main()