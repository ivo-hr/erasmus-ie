#Enrique Juan Gamboa
#D23125488

from typing import List
import csv


class Song:
    title: str = ''
    artist: str = ''
    release_year: str = ''

    #Added defaults for artist and release_year so that the user doesn't have to provide them if they don't have them
    #Force the user to provide a title, as it is the most important part of the song
    def __init__(self, title: str, artist: str = "-", release_year: str = "-"):
        if not title or title == "":
            raise ValueError("Title cannot be empty")
        self.title = title
        self.artist = artist
        self.release_year = release_year

class TunePalAPI:

    songs: List[Song] = [] # holds all songs available from this API
    page_size: int # allows the user to decide how many songs are returned per page

    current_page_index: int
    
    songs_results: List[Song] = [] # holds the current page of song results for the user after a search

    def __init__(self, page_size=None):

        self.page_size = page_size
        #Current page index was never set, so an error would come up when trying to use the API
        self.current_page_index = 0
        with open('songlist.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                title = row['Song Clean']
                artist = row['ARTIST CLEAN']
                release_year = row['Release Year']
                self.songs.append(Song(title, artist, release_year))
            self.songs_results = self.songs

    """Takes a list of songs and returns a smaller window using the 
    current_page_index and page_size"""
    def _build_song_window(self, song_list: List[Song]):
        first_index = self.current_page_index * self.page_size
        last_index = first_index + self.page_size
        return song_list[first_index:last_index]

    """Adds a song, but only if it isn't already in the list"""
    def add_song(self, title: str, artist: str, release_year: str):
        #self.songs.add(Song(artist, title, release_year))
            # No such function as add, use append. Also, the order of the parameters is wrong. 
            # Also never checked if the song is already in the list>
        new_song = Song(title, artist, release_year)
        if new_song not in self.songs:
            self.songs.append(new_song)

    """Return a page of songs, use next_page and previous_page to change the window"""
    def get_songs(self):
        return self._build_song_window(self.songs_results)

    """Tells the API to move to the previous page"""
    def next_page(self):
        #self.current_page_index = self.current_page_index + 1
            #Was using current_page instead ofcurrent_page_index

        self.current_page_index = self.current_page_index + 1

    """Tells the API to move to the next page"""
    def previous_page(self):
        self.current_page_index = self.current_page_index - 1

    """Set the page_size parameter, controllinig how many songs are returned"""
    def set_page_size(self, page_size: int):
        # Never checked if the page size was valid
        if isinstance(page_size, int) and page_size > 0:
            self.page_size = page_size

    """The search() function matches any songs whose title or artist starts
        with the query provided. E.G. a query of "The" would match "The Killers"
        "The Libertines" etc.
    """
    def search(self, starts_with_query: str):
        #Hits might get overwhemled with too many songs, so a global list will store the hits
        hits = []
        for song in self.songs:
            # Never checked for artist, only title
            if song.title.startswith(starts_with_query) or song.artist.startswith(starts_with_query):
                hits.append(song)
            # Get the hits and store them in a global list
            self.songs_results = hits
            
        return self._build_song_window(self.songs_results)

    """Allows users to filter out old-person music. Filter songs to only return
        songs released since a certain date. e.g. a query of 2022 would only return
        songs released this year 
    """
    def get_songs_since(self, release_year: str):
        hits = []
        for song in self.songs:
            #Never checked if the release year was valid. Also the year wasn't being included in the results
            if not song.release_year != "-" or not release_year.isdigit():
                raise TypeError("Invalid release year")
            if song.release_year >= release_year:
                hits.append(song)
        #Get the hits and store them in a global list
        self.songs_results = hits
        return self._build_song_window(self.songs_results)
