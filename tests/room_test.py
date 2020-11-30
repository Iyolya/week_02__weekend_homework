import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):

        self.room1 = Room("Stars Hollow", 10)    

        self.guest1 = Guest("Sally Owens")

        self.song1 = Song("Folsom Prison Blues", "Johnny Cash", "Rock and roll")
        self.song2 = Song("Angel from Montgomery", "Bonnie Raitt", "genre2")
        # self.song3 = Song("title3", "artist3", "genre3")
        # self.song4 = Song("title4", "artist4", "genre4")

    def test_room_has_name(self):
        self.assertEqual("Stars Hollow", self.room1.name)

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room1.capacity)

    def test_number_of_guests(self):  
        self.assertEqual(0, self.room1.number_of_guests())  



