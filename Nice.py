from __future__ import print_function
from Base import Interpreter


class NiceInterpreter(Interpreter):
    def handleError(self, side='left'):
        if side == 'left':
            print("Couldn't find matching right bracket")

        elif side == 'right':
            print("Couldn't find matching left bracket")

        else:
            print("An unknown error occurred.")

    def setChars(self):
        self.gt = '>'
        self.lt = '<'
        self.plus = '+'
        self.minus = '-'
        self.period = '.'
        self.comma = ','
        self.lbracket = '['
        self.rbracket = ']'
