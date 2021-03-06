
"""
Text based adventure, mother fucker.

Need a way to pass things into this like character and levels. This
should be completely agnostic to custom characters, levels, monsters,
and items and just work on anything.
"""

try:
    import simplejson as json
except ImportError:
    import json
import sys
import textwrap
from Adventure import Adventure
from Room import Room
from Parser.langInterp import *

class Mud(object):
    def __init__(self, args):
        self.args = args
        self.prompt = '> '
        self.adventure = None
        self.verbose = self.args.verbose
        if self.args.adventure_file:
            self.adventure = self.loadAdventure(self.args.adventure_file)

    def run(self):
        '''
        Run the game. This will probably end up being where most of the work
        is centralized.
        '''
        while True:
            if self.adventure != None:
                print textwrap.fill("[%s]" % self.adventure.getCurrentRoom().name, 80)
                print textwrap.fill(self.adventure.getCurrentRoom().description, 80)

            user_input = raw_input(self.prompt)
            if user_input == 'quit':
                break
            action, direction = langInterp(user_input)
            self.doAction(action, direction)


    def doAction(self, action = None, direction = None):
        '''
        Do what the user wanted to do.

        Standard actions are:
        - look
        - go [direction]

        `action`: The action to perform.
        `direction`: Direction associated with the action.
        '''
        if self.verbose:
            print "Action: %s\nDirection: %s" % (action, direction)
        if action == 'move' and direction != None:
            self.adventure.goToRoom(direction)
        elif action == 'look':
            pass
        else:
            pass
        return True


    def loadAdventure(self, adventure_file=None):
        '''
        Load an adventure file. Returns an adventure object.

        `adventure_file`: The name of the file to load.
        '''
        try:
            adv_in = json.loads(open(adventure_file, 'r').read())
        except:
            print "Unable to load adventure file %s" % adventure_file
            sys.exit(1)
        rooms = []
        for key in adv_in['rooms']:
            room = Room.Room()
            room._id = key
            room.name = adv_in['rooms'][key]['name']
            room.description = adv_in['rooms'][key]['description']
            room.north = adv_in['rooms'][key]['north']
            room.east = adv_in['rooms'][key]['east']
            room.south = adv_in['rooms'][key]['south']
            room.west = adv_in['rooms'][key]['west']
            rooms.append(room)

        adventure = Adventure.Adventure(adv_in['adventure_name'], rooms, adv_in['entrance_id'])
        return adventure
