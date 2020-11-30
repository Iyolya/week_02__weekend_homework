import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):

        self.guest1 = Guest("Sally Owens")

    def test_guest_has_name(self):
        self.assertEqual("Sally Owens", self.guest1.name)
