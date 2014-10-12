
"""
Mud entry point.
"""

from mud import mud as m

def hello(args):
    mud = m(args)
    mud.hello()
