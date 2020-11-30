import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    song1 = Song("Folsom Prison Blues", "Johnny Cash", "Rock and roll")
    song2 = Song("Angel from Montgomery", "Bonnie Raitt", "genre2")
    song3 = Song("title3", "artist3", "genre3")
    song4 = Song("title4", "artist4", "genre4")

    def test_song_has_title(self):
        self.assertEqual("Folsom Prison Blues", self.song1.title)

    def test_song_has_artist(self):
        self.assertEqual("Johnny Cash", self.song1.artist)

    def test_song_has_genre(self):
        self.assertEqual("Rock and roll", self.song1.genre)



       
    
