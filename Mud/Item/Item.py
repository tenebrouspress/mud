
'''
An item.
'''

class Item(object):

    def __init__(self):
        self.name = None
        self.description = None
        # Effect might be a object that modifies a stat given a condition?
        self.effect = None
