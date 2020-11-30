class Room:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guests = []
        self.songs = []


    def number_of_guests(self):
        return len(self.guests)

    def check_in_guests(self, guest):
        self.guests.append(guest)

    def check_out_guests(self, guest):
        for someone in self.guests:
            if someone == guest:
                self.guests.remove(guest)