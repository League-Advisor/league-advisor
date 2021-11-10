"""This module provides simulation tests for discover module"""

import os
from league_advisor.string_assets.menu_strings import strings

class Discover:

    """
    This class prints rules of the game.

    Methods:

        discover :

            This methods provides the user with discover the rules of the game
            
            Arguments: None

            Return: None
            
      -------------------------------------------------------------------------------------

        get_color_mode:
            
            This method sets the color mode for the module.

            Arguments:

                color_mode: String

                Return: String
    """
    def __init__(self):
        self.mode = ""

    def get_color_mode(self, color_mode):
        self.mode = color_mode
        return self.mode

    def discover(self):

        if self.mode == "c":
            print(strings["disc_color"]) 
        else:
            print(strings["disc"]) 

        user_input = input("> ")
        if user_input or user_input=="":
            clear = lambda: os.system('clear')
            # clear()








