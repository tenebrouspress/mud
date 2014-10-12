
"""
Text based adventure, mother fucker.
"""

class mud(object):
    def __init__(self, args):
        self.args = args
        self.prompt = '> '

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
