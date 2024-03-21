#Enrique Juan Gamboa
#D23125488


import unittest
import os
from tunepalapi import TunePalAPI, Song

class TestTunePalAPI(unittest.TestCase):
    def setUp(self):
        # Change the working directory to the directory of the script to read the CSV file
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        # Initialize the TunePalAPI object for testing
        self.tunepal_api = TunePalAPI(page_size=5)
         #Add some songs to the API
        self.tunepal_api.add_song("The Test Song", "Test Artist", "2022")
        self.tunepal_api.add_song("Test Song 2", "Test Artist 2", "2023")
        self.tunepal_api.add_song("Test Song 3", "Test Artist 3", "2002")
        self.tunepal_api.add_song("Test Song 4", "Test Artist 4", "2022")


    '''
    Purpose: Test if the API is set up correctly
    Focus on:
        TunePalAPI.__init__
    '''
    def test_api_setup(self):
        # Test the initial setup of the API
        self.assertEqual(self.tunepal_api.page_size, 5)
        self.assertEqual(self.tunepal_api.current_page_index, 0)
        self.assertTrue(len(self.tunepal_api.songs) > 0 and isinstance(self.tunepal_api.songs[0], Song))
        #self.assertEqual(self.tunepal_api.songs_results, self.tunepal_api.songs)


    '''
    Purpose: Test if songs are set up correctly
    Focus on:
        Song.__init__
    '''
    def test_song_setup(self):
        # Test the initial setup of the Song
        test_song = Song("On the Rocks", "Ken Ashcorp", "2015")
        self.assertEqual(test_song.title, "On the Rocks")
        self.assertEqual(test_song.artist, "Ken Ashcorp")
        self.assertEqual(test_song.release_year, "2015")

    
    '''
    Purpose: Test if songs are set up correctly when only receiving title
    Focus on:
        Song.__init__
    '''
    def test_song_setup_incomplete(self):
        # Test the initial setup of the Song with incomplete information
        test_song = Song(title="Burgz")
        self.assertEqual(test_song.title, "Burgz")
        self.assertEqual(test_song.artist, "-")
        self.assertEqual(test_song.release_year, "-")

    '''
    Purpose: Test if songs avoid being set up with no title
    Focus on:
        Song.__init__
    '''
    def test_bad_song_setup(self):
        # Test the initial setup of the Song with no title
        with self.assertRaises(ValueError):
            test_song = Song(title="")



    '''
    Purpose: Test if songs can be added to the API
    Focus on:
        TunePalAPI.add_song
    '''
    def test_add_song(self):
        # Test adding a song to the API
        initial_length = len(self.tunepal_api.songs)
        self.tunepal_api.add_song("Test Song", "Test Artist", "2022")
        self.assertEqual(len(self.tunepal_api.songs), initial_length + 1)


    '''
    Purpose: Test if songs can be retrieved correctly paginated from the API
    Focus on:
        TunePalAPI.get_songs
    '''
    def test_get_songs(self):
        # Test getting a page of songs
        songs = self.tunepal_api.get_songs()
        self.assertEqual(len(songs), 5)  # Assuming page_size is set to 5 initially


    '''
    Purpose: Test if the API can move to the next page correctly
    Focus on:
        TunePalAPI.next_page
    '''
    def test_next_page(self):
        # Test moving to the next page
        previous_page = self.tunepal_api.current_page_index
        self.tunepal_api.next_page()
        self.assertEqual(self.tunepal_api.current_page_index, previous_page + 1)

    '''
    Purpose: Test if the API can move to the previous page correctly
    Focus on:
        TunePalAPI.previous_page
    '''
    def test_previous_page(self):
        # Test moving to the previous page
        next_page = self.tunepal_api.current_page_index
        self.tunepal_api.previous_page()
        self.assertEqual(self.tunepal_api.current_page_index, next_page - 1)


    '''
    Purpose: Test if the API can change the page size correctly
    Focus on:
        TunePalAPI.set_page_size
    '''
    def test_set_page_size(self):
         #Test setting the page size
        self.tunepal_api.set_page_size(10)
        self.assertEqual(self.tunepal_api.page_size, 10)
        songs = self.tunepal_api.get_songs()
        self.assertEqual(len(songs), 10)
        self.tunepal_api.set_page_size(5)


    '''
    Purpose: Test if the API can search for songs correctly and return results including the query
    Focus on:
        TunePalAPI.search
    '''
    def test_search(self):
         #Test searching for songs
        result = self.tunepal_api.search("The")
        self.assertIsInstance(result, list)
        self.assertTrue(all(("The" in song.title for song in result) or ("The" in song.artist for song in result)))


    '''
    Purpose: Test if the API can filter songs by release year correctly
    Focus on:
        TunePalAPI.get_songs_since
    '''
    def test_get_songs_since(self):
         #Test filtering songs by release year
        result = self.tunepal_api.get_songs_since("2015")
        self.assertIsInstance(result, list)
        self.assertTrue(all(song.release_year >= "2015" for song in result))


    '''
    Purpose: Test if the API behaves correctly and does not crash when reaching the end of the song list
    Focus on:
        TunePalAPI.next_page
        TunePalAPI.get_songs
    '''
    def test_reach_end_list(self):
         #Test reaching the end of the song list
        self.tunepal_api.current_page_index = len(self.tunepal_api.songs_results) // self.tunepal_api.page_size
        self.assertEqual(len(self.tunepal_api.get_songs()), len(self.tunepal_api.songs_results) % self.tunepal_api.page_size)
        self.tunepal_api.next_page()
        self.assertEqual(len(self.tunepal_api.get_songs()), 0)
        self.tunepal_api.previous_page()
        self.assertEqual(len(self.tunepal_api.get_songs()), len(self.tunepal_api.songs_results) % self.tunepal_api.page_size)
        self.tunepal_api.previous_page()
        self.assertEqual(len(self.tunepal_api.get_songs()), self.tunepal_api.page_size)


    '''
    Purpose: Test if the API behaves correctly and does not crash when reaching the start of the song list
    Focus on:
        TunePalAPI.previous_page
        TunePalAPI.get_songs
    '''
    def test_reach_start_list(self):
         #Test reaching the start of the song list
        self.tunepal_api.current_page_index = 0
        self.assertEqual(len(self.tunepal_api.get_songs()), self.tunepal_api.page_size)
        self.tunepal_api.previous_page()
        self.assertEqual(len(self.tunepal_api.get_songs()), 0)
        self.tunepal_api.next_page()
        self.assertEqual(len(self.tunepal_api.get_songs()), self.tunepal_api.page_size)


    '''
    Purpose: Test if the API behaves correctly and does not crash when adding an existing song
    Focus on:
        TunePalAPI.add_song
    '''
    def test_add_existing_song(self):
        # Test adding an existing song
        initial_length = len(self.tunepal_api.songs)
        self.tunepal_api.add_song(self.tunepal_api.songs[0].title, self.tunepal_api.songs[0].artist, self.tunepal_api.songs[0].release_year)
        self.assertEqual(len(self.tunepal_api.songs), initial_length)

    
    '''
    Purpose: Test if the API behaves correctly and adds a song with repeated title but different artists
    Focus on:
        TunePalAPI.add_song
    '''
    def test_add_new_song_same_title(self):
        # Test adding an existing song
        initial_length = len(self.tunepal_api.songs)
        self.tunepal_api.add_song(self.tunepal_api.songs[0].title, "Other artist", self.tunepal_api.songs[0].release_year)
        self.assertEqual(len(self.tunepal_api.songs), initial_length+1)



    '''
    Purpose: Test if the API correctly builds a song window
    Focus on:
        TunePalAPI._build_song_window
    '''
    def test_build_song_window(self):
        # Test building a song window
        self.tunepal_api.current_page_index = 0
        window = self.tunepal_api._build_song_window(self.tunepal_api.songs_results)
        self.assertTrue(len(window) <= self.tunepal_api.page_size)
        self.assertEqual(self.tunepal_api.songs_results[0], window[0])


    '''
    Purpose: Test if the API correctly builds a song window and retrieves it after moving to the next page
    Focus on:
        TunePalAPI.next_page
        TunePalAPI.get_songs
    '''
    def test_get_songs_next_page(self):
        # Test getting a page of songs after moving to the next page
        songs = self.tunepal_api.get_songs()
        self.assertEqual(songs[0], self.tunepal_api.songs_results[0])
        self.tunepal_api.next_page()
        songs = self.tunepal_api.get_songs()
        self.assertEqual(songs[0], self.tunepal_api.songs_results[self.tunepal_api.page_size])


    '''
    Purpose: Test if the API correctly builds a song window and retrieves it after moving to the previous page
    Focus on:
        TunePalAPI.previous_page
        TunePalAPI.get_songs
    '''
    def test_get_songs_previous_page(self):
        # Test getting a page of songs after moving to the previous page
        self.tunepal_api.next_page()
        songs = self.tunepal_api.get_songs()
        self.assertEqual(songs[0], self.tunepal_api.songs_results[self.tunepal_api.page_size])
        self.tunepal_api.previous_page()
        songs = self.tunepal_api.get_songs()
        self.assertEqual(songs[0], self.tunepal_api.songs_results[0])

    
    '''
    Purpose: Test if the API returns an empty list when there is no match for the query
    Focus on:
        TunePalAPI.search
    '''
    def test_search_nonexisting_query(self):
        result = self.tunepal_api.search("ThisSongDoesNotExist")
        self.assertEqual(result, [])
        self.assertEqual(self.tunepal_api.songs_results, [])


    '''
    Purpose: Test if the API correctly returns all songs when the query is empty
    Focus on:
        TunePalAPI.search
    '''  
    def test_search_empty_query(self):
        result = self.tunepal_api.search("")
        self.assertEqual(len(result), self.tunepal_api.page_size)
        self.assertEqual(len(self.tunepal_api.songs_results), len(self.tunepal_api.songs_results))


    '''
    Purpose: Test if the API correctly returns an empty list when there are no songs released after the given year
    Focus on:
        TunePalAPI.get_songs_since
    '''
    def test_get_songs_since_nonexisting_year(self):
        result = self.tunepal_api.get_songs_since("3000")
        self.assertEqual(result, [])
        self.assertEqual(self.tunepal_api.songs_results, [])

    '''
    Purpose: Test if the API correctly returns an empty list when it does not receive a valid year
    Focus on:
        TunePalAPI.get_songs_since
    '''
    def test_get_songs_since_bad_year(self):
        result = self.tunepal_api.get_songs_since("abc")
        self.assertEqual(result, [])
        self.assertEqual(self.tunepal_api.songs_results, [])


    '''
    Purpose: Test if the API correctly paginates through the results of a search
    Focus on:
        TunePalAPI.search
        TunePalAPI.get_songs
        TunePalAPI.next_page
        TunePalAPI.previous_page
    '''
    def test_paginate_search(self):
        result = self.tunepal_api.search("The")
        self.assertEqual(self.tunepal_api.current_page_index, 0)
        self.assertEqual(len(result), self.tunepal_api.page_size)
        self.assertEqual(result[0], self.tunepal_api.songs_results[0])
        self.tunepal_api.next_page()
        result = self.tunepal_api.get_songs()
        self.assertEqual(result[0], self.tunepal_api.songs_results[self.tunepal_api.page_size])
        self.tunepal_api.previous_page()
        result = self.tunepal_api.get_songs()
        self.assertEqual(result[0], self.tunepal_api.songs_results[0])


    '''
    Purpose: Test if the API correctly paginates through the results of a get_songs_since
    Focus on:
        TunePalAPI.get_songs_since
        TunePalAPI.get_songs
        TunePalAPI.next_page
        TunePalAPI.previous_page
    '''
    def test_paginate_get_songs_since(self):
        result = self.tunepal_api.get_songs_since("1980")
        self.assertEqual(self.tunepal_api.current_page_index, 0)
        self.assertEqual(len(result), self.tunepal_api.page_size)
        self.assertEqual(result[0], self.tunepal_api.songs_results[0])
        self.tunepal_api.next_page()
        result = self.tunepal_api.get_songs()
        self.assertEqual(result[0], self.tunepal_api.songs_results[self.tunepal_api.page_size])
        self.tunepal_api.previous_page()
        result = self.tunepal_api.get_songs()
        self.assertEqual(result[0], self.tunepal_api.songs_results[0])


    '''
    Purpose: Test if the API avoids setting a bad page size
    Focus on:
        TunePalAPI.set_page_size
    '''
    def test_set_bad_page_size(self):
        # Test setting the page size to a bad value
        self.tunepal_api.set_page_size(5) #Initial correct page size
        self.tunepal_api.set_page_size("abc")
        self.assertEqual(self.tunepal_api.page_size, 5)
        self.tunepal_api.set_page_size(0)
        self.assertEqual(self.tunepal_api.page_size, 5)
        self.tunepal_api.set_page_size(-1)
        self.assertEqual(self.tunepal_api.page_size, 5)
        self.tunepal_api.set_page_size(5.4)
        self.assertEqual(self.tunepal_api.page_size, 5)
        with self.assertRaises(TypeError):  
            self.tunepal_api.set_page_size()

