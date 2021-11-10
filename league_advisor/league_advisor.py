
"""This module runs the core functions of the program"""

from league_advisor.input_handler import InputHandler
from league_advisor.string_assets.menu_strings import strings
import os

class LeagueAdvisor:
    """
    This class handles the core functionality of League Advisor program.

    Methods:

      run_program:

        Runs a sequence of functions and methods that operate League Advisor program.
        Welcomes the user when he starts the program and prompts him for an input.
        Requires the user for accurate input if he enters an invalid command.

        Arguments: None

        Return: None
    """

    def __init__(self):
        self.input_handler = InputHandler()
        self.welcome_flag = True
        self.mode = ""

    def run_program(self):

        if self.welcome_flag == True:
            self.welcome_flag = False
            self.input_handler.welcome_message()
            self.mode = self.input_handler.color_mode()
            if self.mode.lower() == "c" or self.mode.lower() == "color" or self.mode.lower() == "colour":
                self.mode = "c"
            if self.mode or self.mode=="":
                clear = lambda: os.system('clear')
                clear()
                   
        self.input_handler.input_flag = False

        while not self.input_handler.input_flag:
            if self.mode == "c":
                print(strings["main_menu_color"])
                self.input_handler.prompt_user()
                self.input_handler.input_interpreter(self.input_handler.user_input)

            else:
                print(strings["main_menu"])
                self.input_handler.prompt_user()
                self.input_handler.input_interpreter(self.input_handler.user_input)

if __name__ == "__main__":

    league_advisor = LeagueAdvisor()
    league_advisor.run_program()