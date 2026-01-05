import storage

# Global variable containing a set to tell what genres are defined in the system
GENRES = {"ambient","synthwave","rock","indie Pop","lo-fi","dance","experimental","other"}

class Track:
    # Define a simple constructor for Track
    # the artist argument can accept one author or list of them
    def __init__(self, artist, title, genre, duration, lufs):
        # Validate artist
        if not isinstance(artist, (str, list)) or not artist:
            raise ValueError("Artist must be a non-empty string or list of strings")
        
        # Validate title
        if not isinstance(title, str) or not title:
            raise ValueError("Title must be a non-empty string")
        
        # Validate genre
        if not isinstance(genre, str) or not genre:
            raise ValueError("Genre must be a non-empty string")
        
        # Validate length
        if not isinstance(duration, tuple) or not all(isinstance(n, int) and n >= 0 for n in duration): # pure function to tell that both pair values must be ints
            raise ValueError("Duration must be a pair of positive integers")
        
        # Validate LUFS
        if not isinstance(lufs, (int, float)):
            raise ValueError("LUFS must be a number")
        

        # Handle a singe value or a list
        # each word in an artist name must be capitalized, not all lowercase/uppercase
        if type(artist) is list:
            self.artist = [n.title() for n in artist]
        else:
            self.artist = [artist.title()]

        # Initialize the song title
        self.title = title.title() # each word in a title must be capitalized, not all lowercase/uppercase

        # If the genre is not defined in the system save as "Other" genre
        # genre check is not case sesnitive and the final value is capitalized
        if genre.lower() in GENRES:
            self.genre = genre.capitalize()
        else:
            self.genre = "Other"

        # Works with (minutes, seconds) pairs
        self.duration = duration

        # Loudness Units relative to Full Scale (LUFS) used to show human percieved loudness as opposed to naive decibels
        self.lufs = lufs
    
    # Define how the Track instance should be printed
    def __str__(self):
        # Add just one artist or list them seperated with "&"
        artist_str = " & ".join(self.artist)
        
        return f"{artist_str} - {self.title} ({self.duration[0]}:{self.duration[1]:02}, {self.genre}, {self.lufs} LUFS)"

    # Called on each element when it's printed inside a list
    def __repr__(self):
        return str(self)
    
    # Create an remix instance of a song
    @storage.log("remix_logs")
    def remix(self, artist, genre, duration, lufs):
        return Track(artist, self.title+" Remix", genre, duration, lufs)
    