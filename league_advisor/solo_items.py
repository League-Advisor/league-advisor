"""this module will choose the optimal items for the champion shich the user choosed"""

import requests
from bs4 import BeautifulSoup
from league_advisor.string_assets.menu_strings import strings


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

    """

    def __init__(self):
        self.user_input = ""

    def prompt_user(self):
        self.user_input = input("> ").lower()

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
        print(settied_items)
        return settied_items

    def direct_input(self):

        print("Enter your champion name or type b to go back or q to quit")
        while True:
            self.prompt_user()
            if self.user_input == "b" or self.user_input == "back":
                return self.user_input
            elif self.user_input == "q" or self.user_input == "quit":
                print(
                    """Thank you for using League Advisor. Hope to see you again soon!""")
                quit()
            elif not self.user_input in strings["champion_list_lower"]:
                print("please enter a valid name")
                continue
            else:
                print("proccessing...")
                self.get_items(self.user_input)
                print("enter any key to go back...")
                self.prompt_user()
                return "b"
