
"""
Python-based mud games.
"""

class mud(object):
    def __init__(self, args):
        self.args = args
        self.prompt = '> '

    def run(self):
        while True:
            user_input = raw_input(self.prompt)

            if user_input == 'quit':
                break

            ## do something with user_input
