class Room:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guests = []
        self.songs = []


    def number_of_guests(self):
        return len(self.guests)