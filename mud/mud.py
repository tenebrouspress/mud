
"""
Text based adventure, mother fucker.

Need a way to pass things into this like character and levels. This
should be completely agnostic to custom characters, levels, monsters,
and items and just work on anything.
"""

import json
from adventure import adventure
from room import room
from parser.langInterp import *

class mud(object):
    def __init__(self, args):
        self.args = args
        self.prompt = '> '
        self.adventure = None
        if self.args.adventure_file:
            self.adventure = self.load_adventure(self.args.adventure_file)

    def run(self):
        '''
        Run the game. This will probably end up being where most of the work
        is centralized.
        '''

        if self.adventure != None:
            print self.adventure.getCurrentRoom().description

        while True:
            user_input = raw_input(self.prompt)

            if user_input == 'quit':
                break

            action, direction = langInterp(user_input)
            print "Action: %s\nDirection: %s" % (action, direction)

    def load_adventure(self, adventure_file=None):
        adv_in = json.loads(open(adventure_file, 'r').read())
        rooms = []
        for key in adv_in['rooms']:
            new_room = room.room()
            new_room._id = key
            new_room.name = adv_in['rooms'][key]['name']
            new_room.description = adv_in['rooms'][key]['description']
            rooms.append(new_room)

        game_adventure = adventure.adventure(adv_in['adventure_name'], rooms, adv_in['entrance_id'])
        return game_adventure
