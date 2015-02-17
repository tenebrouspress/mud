
'''
An adventure.
'''

class Adventure(object):
    def __init__(self, name=None, rooms=None, entrance_id=None):
        self.name = name
        self.rooms = rooms
        self.current_room = entrance_id


    def setCurrentRoom(self, current_room=None):
        self.current_room = current_room

    def getCurrentRoom(self,current_room = None):
        for room in self.rooms:
            if room._id == self.current_room:
                current_room = room
        return current_room

    def goToRoom(self, direction=None):
        current_room = None
        for room in self.rooms:
            if "north" == direction:
                self.setCurrentRoom(room.north)
            if "south" == direction:
                self.setCurrentRoom(room.south)
            if "east" == direction:
                self.setCurrentRoom(room.east)
            if "west" == direction:
                self.setCurrentRoom(room.west)
