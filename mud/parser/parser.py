
"""
The mud parser.
"""

import argparse
import mud.mud


class parser(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='MUDS')
        self.parser.add_argument('-v', dest='verbose', action='store_true', help='Show verbose output')
        self.parser.set_defaults(m=mud.hello)
