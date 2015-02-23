
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

    def getCurrentRoom(self, current_room=None):
        for room in self.rooms:
            if room._id == self.current_room:
                current_room = room
        return current_room

    def getRoom(self, room_id=None):
        the_room = None
        for room in self.rooms:
            if room._id == room_id:
                the_room = room
        return the_room

    def goToRoom(self, direction=None):
        if direction == 'north':
            self.setCurrentRoom(self.getCurrentRoom().north)
        elif direction == 'east':
            self.setCurrentRoom(self.getCurrentRoom().east)
        elif direction == 'south':
            self.setCurrentRoom(self.getCurrentRoom().south)
        else:
            self.setCurrentRoom(self.getCurrentRoom().west)
