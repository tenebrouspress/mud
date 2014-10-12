
"""
Text based adventure, mother fucker.

Need a way to pass things into this like character and levels. This
should be completely agnostic to custom characters, levels, monsters,
and items and just work on anything.
"""

class mud(object):
    def __init__(self, args):
        self.args = args
        self.prompt = '> '
        self.current_room = None

    def run(self):
        '''
        Run the game. This will probably end up being where most of the work
        is centralized.
        '''

        while True:
            user_input = raw_input(self.prompt)

            if user_input == 'quit':
                break

            ## do something with user_input

    def load_adventure(self, adventure_file=None):
        ## load an adventure file?
        pass
