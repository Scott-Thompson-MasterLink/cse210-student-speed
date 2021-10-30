import random
from game import constants
from game.actor import Actor
from game.point import Point
from game.input_service import InputService

class Buffer(Actor, InputService):
    """The Buffer's responsability is to keep track of the user's inputs and display them in the formatted output.

    Attributes:
        _point (int): keeps track of the score.
        _position (Point): an instance of Point.
        _inputs (string): The user's inputs.
        _buffer (string): sets the text to the bottom.
    """
    
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._points = 0     
        self._position = Point(1, constants.MAX_Y)
        self._inputs = ''
        self._buffer = super().set_text(f'Buffer: {self._inputs}')

    def get_input(self):
        """Gets the input.
        
        Args:
            self (Buffer): An instance of Buffer.
            
        Returns:
            string: inputs.
        """
        
        return self._inputs

    def set_input(self):
        """Updates the buffer text to the given value.
        
        Args:
            self (Buffer): An instance of Buffer.
            letter (string): The given value.
        """

        letter = super().get_letter()
        if letter == '*':
            self._inputs = ''
        else:
            self._inputs = letter

    #for Director within _get_inputs(self): self._buffer.set_input()

    def get_points(self):
        """Gets the points.
        
        Args:
            self (Buffer): an instance of Buffer.

        Returns:
            points: the points obtained 
        """

        return self._points

    def set_points(self):
        """Sets the points.
        
        Args:
            self (Buffer): an instance of Buffer.

        Returns:
            points: random points obtained 
        """

        self._points += random.randint(1, 5)


    
