
'''
An adventure.
'''

class adventure(object):
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
