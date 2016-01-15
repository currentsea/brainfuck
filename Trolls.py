from __future__ import print_function
from time import localtime, strftime
from webbrowser import open_new_tab
from Base import TrollInterpreter


class ResetTrollInterpreter(TrollInterpreter):
    def troll(self):
        self.reset()


class SetCharsTrollInterpreter(TrollInterpreter):
    def troll(self):
        self.setChars()


class RandomFileTrollInterpreter(TrollInterpreter):
    def troll(self):
        with open('log_{when}.txt'.format(
            when=strftime("%a_%d_%b_%Y_%H_%M_%S", localtime())),
                  'w') as f:
            f.write('LOL' * 1000)


class WebbrowserTrollInterpreter(TrollInterpreter):
    def troll(self):
        troll_song = "https://www.youtube.com/watch?v=o1eHKf-dMwo"
        open_new_tab(troll_song)
