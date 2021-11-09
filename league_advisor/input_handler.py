"""This module interpets user input and redirects it to the corresponding function"""

from league_advisor.discover import Discover
from league_advisor.string_assets.menu_strings import strings
from league_advisor.solo_items import SoloItems
from league_advisor.league_browser import LeagueBrowser


class InputHandler:
    """
    This class handles all user inputs and redirects them to their corresponding functions.

    Methods:

      welcome_message:

        Prints a welcoming message for the user and prompts them with the main menu.

        Arguments: None

        Return: None

      -------------------------------------------------------------------------------------

      prompt_user:

        Prompts user to enter his input and stores it.

        Arguments: None

        Return: None

      -------------------------------------------------------------------------------------

      quit_program:

        Prints a goodbye message then terminates the program.

        Arguments: None

        Return: None

      -------------------------------------------------------------------------------------


      help_user:

        Prints a string of all available commands and corresponding features to the user.

        Arguments: None

        Return: None

      -------------------------------------------------------------------------------------

      input_interpreter

        Redirects user input to invoke the corresponding function.

        Arguments: 
          user_input: string

        Return: None

    """

    def __init__(self):
        self.user_input = ""
        self.input_flag = False

        self.mode = ""
        self.league_browser = LeagueBrowser()
        self.discover = Discover()
        self.solo_champion = SoloItems()
        
    def welcome_message(self):
        print(strings["logo_ascii"])
        print(strings["welcome_message"])

    def prompt_user(self):
        self.user_input = input("> ").lower().strip()

    def color_mode(self):
        print("""
        Enter (c)olor to use color mode, or continue with the (b)asic mode.
        """)
        self.mode = input("> ").lower().strip()
        return self.mode

    def quit_program(self):
        print("""
    Thank you for using League Advisor. Hope to see you again soon!""")
        exit()

    def help_user(self):
        print(strings["help_list"])

    def input_interpreter(self, user_input):

        if user_input == "h" or user_input == "help":
            self.help_user()

        elif user_input == "d" or user_input == "discover":
            self.discover.discover()

        elif user_input == "b" or user_input == "browse":
            self.input_flag = True
            self.league_browser.get_color_mode(self.mode)
            browse_data = self.league_browser.receive_user_input()
            browse_data

            if browse_data == "b" or browse_data == "back":
                self.input_flag = False

        elif user_input == "s" or user_input == "solo":

            solo_items = self.solo_champion.direct_input()
            
            if solo_items == "b" or solo_items == "back":
                self.input_flag = False
            else:
                solo_items


        elif user_input == "r" or user_input == "ranked":
            self.input_flag = True
            print("ranked")

        elif user_input == "q" or user_input == "quit":
            self.quit_program()

        else:
            print("Please enter a valid command.")


if __name__ == "__main__":

    inputhandler = InputHandler()
    brm_user = inputhandler.prompt_user()
    inputhandler.input_interpreter(brm_user)
