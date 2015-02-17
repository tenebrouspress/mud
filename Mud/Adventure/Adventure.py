
'''
An adventure.
'''

class Adventure(object):
    def __init__(self, name=None, rooms=None, entrance_id=None):
        self.name = name
        self.rooms = rooms
        self.current_room = entrance_id

    def getCurrentRoom(self):
        current_room = None
        for room in self.rooms:
            if room._id == self.current_room:
                current_room = room
        return current_room

    def goToRoom(self, direction=None):
        for room in self.rooms:
            if "north" == direction:
                self.current_room = room.north
            if "south" == direction:
                self.current_room = room.south
            if "east" == direction:
                self.current_room = room.east
            if "west" == direction:
                self.current_room = room.west
