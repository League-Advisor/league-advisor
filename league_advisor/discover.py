"""This module provides the user with discover the rules of the game"""
import os
from league_advisor.string_assets.menu_strings import strings

class Discover:

    """
    This class handles the rules of the game.

    Methods:

        discover :

            This methods provides the user with discover the rules of the game
            
            Arguments: None

            Return: None
    """
    def __init__(self):
        pass


    def discover(self):
        print(strings["desc"]) 
        user_input = input("> ")
        if user_input :
            clear = lambda: os.system('clear')
            clear()
          








