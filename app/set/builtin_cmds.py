import sys

from app.command import Cmd
from app.output import bye


# This command simply ends program
class Exit(Cmd):
    def invoke(self, params):
        bye()
        sys.exit()


# This command tries to connect with EaseCI core in specified address, credentials etc.
class Connect(Cmd):
    def invoke(self, params):
        print('Teraz wywołuję komende connect wraz z takimi opcjami: ' + str(params))
