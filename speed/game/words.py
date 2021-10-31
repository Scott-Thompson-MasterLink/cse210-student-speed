import random
from game.actor import Actor
from game.point import Point
from game import constants
from speed.game import score

words = constants.LIBRARY

class Word(Actor):
    _words = words
    def __init__(self):
        super().__init__()
        self._word = ''
        self.get_new_word()
        self._x = random.randint(1, constants.MAX_X)
        self._y = random.randint(1, constants.MAX_Y - 1)
        self._position = Point(self._x, self._y)


    def get_word(self):
        return self._word

    def get_new_word(self):
        self._word = random.choice(self._words)
        self.set_text( self._word)

    def set_word_velocity(self):
        
        self._x = (1 + (self._x - 1) % (constants.MAX_X - 1)) + 1
        self._position = Point(self._x, self._y)

    def compare_word(self, word_str):
        if self._word in word_str:
            score = len(self._word)
            self.get_new_word()
            return score
        else:
            return 0

    