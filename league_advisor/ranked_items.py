"""This module will get user choice and comapre it with the list of champions and then send it to data analysis module to pick the optimal items for the user with respect to user team champions also with respect to enemy team champions"""

from league_advisor.string_assets.menu_strings import strings
from league_advisor.string_assets.colors import color
import os


class RankedItem:
    """This module will direct the user input to the match data analysis module

     Methods:
    ---

      prompt_user:

      this method will ask the user to input names of champion separting them with comma and checking for their validity.

      Arguments: None

      Return: None
     ---

        get_color_mode:

            This method sets the color mode for the module.

            Arguments:

                color_mode: String

                Return: String

    ---

        clear:

            This method clears the screen.

            Arguments: None

            Return: None                     
    """

    def __init__(self):
        self.user_response = ""
        self.team = []
        self.enemy = []
        self.analysis_data = []
        self.champion = ""
        self.mode = ""

    def get_color_mode(self, color_mode):
        self.mode = color_mode
        return self.mode

    def clear(self):
        def clear(): return os.system('clear')
        clear()

    def prompt_user(self):

        while not len(self.team) == 5:
            if self.mode == "c":

                print()
                print("Enter your team composition, seperated by commas.")
                print()
                print(
                    f"{color.YELLOW}[Support,Adc,Mid,Jungle,Top]{color.RESET}")
                print()
                print(
                    f"To stop the program, enter ({color.RED}q{color.RESET})uit || ({color.RED}b{color.RESET})ack to the main menu.")

            else:
                print()
                print("Enter your team composition, seperated by commas.")
                print()
                print("Support,Adc,Mid,Jungle,Top")
                print()
                print("To stop the program, enter (q)uit || (b)ack to the main menu.")

            self.user_response = input("> ")

            if self.user_response.lower().strip() == "b" or self.user_response.lower().strip() == "back":
                self.clear()
                return self.receive_item()

            if self.user_response.lower().strip() == "q" or self.user_response.lower().strip() == "quit":
                print("""
                        Thank you for using League Advisor. Hope to see you again soon!""")
                quit()

            if len(self.user_response.split(',')) == 5:
                self.team = self.user_response.split(',')

            for i in range(len(self.team)):
                if not self.team[i].lower().strip() in strings["champion_list_lower"]:
                    self.team = []
                    break

            if not len(self.team) == 5:
                if self.mode == "c":
                    print(
                        f"{color.RED}Please enter a valid composition.{color.RESET}")
                else:
                    print("Please enter a valid composition.")
                continue

            else:

                while True:
                    if self.mode == "c":
                        print()
                        print(
                            f"{color.YELLOW}Enter your current champion name.{color.RESET}")
                        print()
                    else:
                        print()
                        print("Enter your current champion name.")
                        print()

                    self.user_response = input("> ")

                    if not self.user_response.lower().strip() in [name.lower() for name in self.team] or not self.user_response.lower().strip() in strings["champion_list_lower"]:
                        if self.mode == "c":
                            print(
                                f"{color.RED}Enter your champion name correctly.{color.RESET}")
                        else:
                            print("Enter your champion name correctly.")
                        continue

                    else:
                        self.champion = self.user_response
                        break

                while not len(self.enemy) == 5:

                    print()
                    print("Enter your enemy composition, seperated by commas.")
                    print()
                    if self.mode == "c":
                        print(
                            f"{color.YELLOW}Support,Adc,Mid,Jungle,Top{color.RESET}")
                    else:
                        print("Support,Adc,Mid,Jungle,Top")
                    print()
                    self.user_response = input("> ")

                    if self.user_response.lower().strip() == "b" or self.user_response.lower().strip() == "back":
                        self.clear()
                        return self.receive_item()

                    if self.user_response.lower().strip() == "q" or self.user_response.lower().strip() == "quit":
                        print("""
                                Thank you for using League Advisor. Hope to see you again soon!""")
                        quit()

                    if len(self.user_response.split(',')) == 5:
                        self.enemy = self.user_response.split(',')

                    for i in range(len(self.enemy)):
                        if self.enemy[i].lower().strip() in [name.lower() for name in self.team]:
                            if self.mode == "c":
                                print(
                                    f"{color.RED}Please enter a valid composition. One champion cannot be on both teams.{color.RESET}")
                            else:
                                print(
                                    "Please enter a valid composition. One champion cannot be on both teams.")
                            self.enemy = []
                            break

                        if not self.enemy[i].lower().strip() in strings["champion_list_lower"]:
                            self.enemy = []
                            break

                    if not len(self.enemy) == 5:
                        if self.mode == "c":
                            print(
                                f"{color.RED}Please enter a valid composition.{color.RESET}")
                        else:
                            print("Please enter a valid composition.")
                        continue
                    else:
                        self.analysis_data.append(self.team)
                        self.analysis_data.append(self.enemy)
                        self.analysis_data.append(self.champion)

                        for i in range(2):
                            for j in range(len(self.analysis_data[i])):
                                self.analysis_data[i][j] = self.analysis_data[i][j].title(
                                )
                        self.analysis_data[2] = self.analysis_data[2].title()
                        return(self.analysis_data)
