import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):

        self.room1 = Room("Stars Hollow", 10)    

        self.guest1 = Guest("Sally Owens")

        self.song1 = Song("Folsom Prison Blues", "Johnny Cash", "Rock and roll")


    def test_room_has_name(self):
        self.assertEqual("Stars Hollow", self.room1.name)

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room1.capacity)

    def test_number_of_guests(self):  
        self.assertEqual(0, self.room1.number_of_guests())  

    def test_guest_checked_in(self):
        self.room1.check_in_guests(self.guest1)
        self.assertEqual(1, self.room1.number_of_guests())

    def test_guest_checked_out(self):
        self.room1.check_out_guests(self.guest1)
        self.assertEqual(0, self.room1.number_of_guests())

    def test_song_added(self):
        self.room1.add_song(self.song1)
        self.assertEqual(1, self.room1.number_of_songs())





