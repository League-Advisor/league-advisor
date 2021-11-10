"""this module will choose the optimal items for the champion shich the user choosed"""

import os
import requests
from bs4 import BeautifulSoup
from league_advisor.string_assets.menu_strings import strings
from league_advisor.string_assets.colors import color


class SoloItems:
    """
    This class handles the Functionality of choosing the optimal items for the champions in solo mode

    Methods:
     ---------------------------------------------------------------------------------
      prompt_user:

        Prompts user to enter his input and stores it.

        Arguments: None

        Return: None   
     ----------------------------------------------------------------------------------
      get_items:

        this method will scrabe a website in order to get the best items for the given champion 

        Arguments: string champion_name 

        Return: list of optimal items 
     ---------------------------------------------------------------------------------
      direct_input: 

        this method direct the user input to correspounding get_item method

        Argument: None 
        
        Return: list of times 
     ---------------------------------------------------------------------------------

        clear:
            
            This method clears the screen.

            Arguments: None

            Return: None

    """

    def __init__(self):
        self.user_input = ""
        self.mode = ""

    def prompt_user(self):
        self.user_input = input("> ")

    # def clear(self):
    #     clear = lambda: os.system('clear')
    #     clear()
    #     return

    def get_color_mode(self, color_mode):
        self.mode = color_mode
        return self.mode

    def get_items(self, champion_name):
        url = f"https://rankedboost.com/league-of-legends/build/{champion_name}/"
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')
        with open("league_advisor/string_assets/string_file.txt", "w+") as f:
            f.write(str(soup))
        with open("league_advisor/string_assets/html.html", "w+") as f:
            f.write(soup.prettify())
        with open("league_advisor/string_assets/html.html", "r") as f:
            soup = BeautifulSoup(f, "html.parser")

        items_list = strings["item_list"]

        solo_items = []

        for link in soup.find_all("img"):
            item = link.get("title")
            if item in items_list:
                solo_items.append(item)

        settied_items = []
        for i in solo_items:
            if i not in settied_items:
                settied_items.append(i)
        
        if self.mode == "c":
            print(f"{color.YELLOW}['Starter Item', 'Item1', 'Item2', 'Item3', 'Item4', 'Item5', 'Item6']{color.RESET}")
            print()
            print()
            print(f"{color.MAGENTA}{settied_items}{color.RESET}")
            print()
            print()

            return settied_items

        else:
            print("['Starter Item', 'Item1', 'Item2', 'Item3', 'Item4', 'Item5', 'Item6']")
            print()
            print()
            print(settied_items)
            print()
            print()
            
            return settied_items

    def direct_input(self):

        if self.mode == "c":
            print(f"""Enter your champion name to get their optimal build.
            You can still go ({color.RED}b{color.RESET})ack or ({color.RED}q{color.RESET})uit the program.""")
            print()

        else:
            print("""Enter your champion name to process their optimal build path.
            You can still go (b)ack or (q)uit the program.""")
            print()
        while True:
            self.prompt_user()
            if self.user_input.lower().strip() == "b" or self.user_input.lower().strip() == "back":
                return self.user_input
            elif self.user_input.lower().strip() == "q" or self.user_input.lower().strip() == "quit":
                print(
                    """Thank you for using League Advisor. Hope to see you again soon!""")
                quit()
            elif not self.user_input.lower().strip() in strings["champion_list_lower"]:
                print("please enter a valid name")
                continue
            else:
                try:
                    if self.mode == "c":
                        print()
                        print()
                        print(f"{color.GREEN}Processing...{color.RESET}")
                        print()
                        print()

                    else:
                        print()
                        print("Proccessing...")
                    self.get_items(self.user_input.lower().strip())
                    print()
                    print("Enter any key to go back...")
                    self.prompt_user()
                    # self.clear()
                    return "b"
                except:
                    if self.mode == "c":
                        print(f"{color.RED}Connection error... Please try again in a moment.{color.RESET}")                    
                    else:
                        print("Connection error... Please try again in a moment.")
                    self.prompt_user()
                    # self.clear()
                    return "b"
