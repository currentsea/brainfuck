from __future__ import print_function
from random import choice
from sys import stdin


class Interpreter(object):
    # Do not override
    def __init__(self):
        self.reset()
        self.setChars()

    # Override if necessary
    def execute(self, code):
        return self.interpret(code)

    # Do not override
    def getChar(self):
        self.array[self.ptr] = ord(stdin.read(1))

    # Override in subclasses
    # Handles parentheses errors
    def handleError(self):
        raise NotImplementedError

    # Do not override
    def interpret(self, code):
        stdout = False
        index = 0

        while index < len(code):
            char = code[index]

            if char == self.gt:
                self.ptr = (self.ptr + 1) % len(self.array)
                index += 1

            elif char == self.lt:
                self.ptr = (self.ptr - 1) % len(self.array)
                index += 1

            elif char == self.plus:
                self.array[self.ptr] = (self.array[self.ptr] + 1) % 128
                index += 1

            elif char == self.minus:
                self.array[self.ptr] = (self.array[self.ptr] - 1) % 128
                index += 1

            elif char == self.period:
                self.putChar()
                stdout = True
                index += 1

            elif char == self.comma:
                self.getChar()
                index += 1

            elif char == self.lbracket:
                paren = 1

                if self.array[self.ptr] == 0:
                    index += 1

                    while paren != 0 and index < len(code):
                        char = code[index]

                        if char == self.lbracket:
                            paren += 1

                        elif char == self.rbracket:
                            paren -= 1

                        index += 1

                    if index == len(code) and paren != 0:
                        self.handleError(side='left')
                        break

                index += 1

            elif char == self.rbracket:
                paren = -1

                if self.array[self.ptr] != 0:
                    index -= 1

                    while paren != 0 and index >= 0:
                        char = code[index]

                        if char == self.lbracket:
                            paren += 1

                        elif char == self.rbracket:
                            paren -= 1

                        index -= 1

                    if index < 0 and paren != 0:
                        self.handleError(side='right')
                        break

                index += 1

            else:
                index += 1

        return stdout

    # Do not override
    def putChar(self):
        char = self.array[self.ptr]
        print(chr(char), end='')

    # Do not override
    def reset(self):
        self.ptr = 0
        self.array = [0] * 30000

    # Override in subclasses
    def setChars(self):
        # These are the attributes
        # that MUST be defined in
        # this method
        self.gt = None
        self.lt = None
        self.plus = None
        self.minus = None
        self.period = None
        self.comma = None
        self.lbracket = None
        self.rbracket = None


gt_signs = ['>', 'a', 'b', 'c', '1']
lt_signs = ['<', 'd', 'e', 'f', '2']
plus_signs = ['+', 'g', 'h', 'i', '3']
minus_signs = ['-', 'j', 'k', 'l', '4']
period_signs = ['.', 'm', 'n', 'o', '5']
comma_signs = [',', 'p', 'q', 'r', '6']
lbracket_signs = ['[', 's', 't', 'u', '7']
rbracket_signs = [']', 'v', 'w', 'x', '8']


class TrollInterpreter(Interpreter):
    # Do not override
    def handleError(self, side='left'):
        print("Your code is broken. It failed.")

    # Do not override
    def execute(self, code):
        if code == "HELP":
            self.printDirective()

        else:
            stdout = self.interpret(code)
            self.troll()

            return stdout

    # Do not override
    def printDirective(self):
        print("\nLONG LIVE THE TROLL!\n")

        for alias, char in self.aliases.items():
            print("       {alias} --> {char}".format(
                alias=alias, char=char))

        print("\nLONG LIVE THE TROLL!\n")

    # Do not override
    def setChars(self):
        self.gt = choice(gt_signs)
        self.lt = choice(lt_signs)
        self.plus = choice(plus_signs)
        self.minus = choice(minus_signs)
        self.period = choice(period_signs)
        self.comma = choice(comma_signs)
        self.lbracket = choice(lbracket_signs)
        self.rbracket = choice(rbracket_signs)

        self.aliases = {
            self.gt: '>',
            self.lt: '<',
            self.plus: '+',
            self.minus: '-',
            self.period: '.',
            self.comma: ',',
            self.lbracket: '[',
            self.rbracket: ']',
        }

    # Override in subclasses
    def troll(self):
        raise NotImplementedError
