"""This module runs the core functions of the program"""

from league_advisor.input_handler import InputHandler
from league_advisor.string_assets.menu_strings import strings


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

    def run_program(self):
        self.input_handler.input_flag = False

        if self.welcome_flag == True:
            self.welcome_flag = False
            self.input_handler.welcome_message()

        while not self.input_handler.input_flag:
            print(strings["main_menu"])
            self.input_handler.prompt_user()
            self.input_handler.input_interpreter(self.input_handler.user_input)


x = LeagueAdvisor()
x.run_program()
