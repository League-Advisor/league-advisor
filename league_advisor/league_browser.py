""" This module will preview the dataset that the user selected to browes"""

from league_advisor.string_assets.items import items_ascii
from league_advisor.string_assets.items_color import items_color_ascii

from league_advisor.string_assets.colors import color
import json
import re

class LeagueBrowser:
    """This class handles the user inputs to preview the latest version of items and stats.

    Methods:
    ---

      prompt_user:

        Saving the user prompts in the constructer argument.

        Arguments: None

        Return:  None

    ---

      receive_user_input:

        Redirects user input to invoke the corresponding function.

        Arguments: None

        Returns:  user_response, invoke receive_champions() or receive_item(); depend on the user_response.

    ---

      receive_item:

        Preview items depend on which item class the user chooses.

        Arguments: None

        Return: invoke receive_user_input() depend on the user_response.

    ---

      receive_champions:

        Preview champions depend on which champions tag the user chooses.

        Arguments: None

        Return: invoke receive_user_input() depend on the user_response
    """

    def __init__(self):
        self.user_response = ""
        self.user_choise = []
        self.description = ""
        self.mode = ""

    def prompt_user(self):
        self.user_response = input("> ")

    def get_color_mode(self, color_mode):
        self.mode = color_mode
        return self.mode

    def receive_user_input(self):
        if self.mode == "c":
            print()
            print(f"Would you like to preview ({color.RED}i{color.RESET})tems or ({color.RED}c{color.RESET})hampions?")
            print(f"To stop the program, enter ({color.RED}q{color.RESET})uit || ({color.RED}b{color.RESET})ack to the main menu.")            
        else:
            print()
            print("Would you like to preview (i)tems or (c)hampions?")
            print("To stop the program, enter (q)uit || (b)ack to the main menu.")


        while True:
            self.prompt_user()
            if self.user_response.lower().strip() == "i" or self.user_response.lower().strip() == "items":
                return self.receive_item()

            elif self.user_response.lower().strip() == "c" or self.user_response.lower().strip() == "champions":
                return self.receive_champions()

            elif self.user_response.lower().strip() == "b" or self.user_response.lower().strip() == "back":
                return self.user_response

            elif self.user_response.lower().strip() == "q" or self.user_response.lower().strip() == "quit":
                exit()
            else:
                print("Please enter a valid command.")

    def receive_item(self):
        if self.mode == "c":
            print()
            print("*** Which item class would you like to check from the list below? ***")
            print()
        else:
            print()
            print("*** Which item class would you like to check from the list below? ***")
            print()

        item_classes = ["Move Speed", "Base Mana Regen", "Base Health Regen", "Health", "Critical Strike Chance", "Ability Power", "Mana", "Armor", "Magic Resist",
                        "Omnivamp", "Attack Damage", "Attack Speed", "Life Steal", "Armor Penetration", "Lethality", "Ability Haste", "Physical Vamp", "Tenacity"]

        if self.mode == "c":
            items = (",".join(item_classes).replace(',', " || ").replace(",", " "))
            print(f"{color.GREEN} {items} {color.RESET}")
        else:
            print(",".join(item_classes).replace(',', " || ").replace(",", " "))
            print()

        while not self.user_response.lower().strip() in [item.lower() for item in item_classes]:
            self.prompt_user()

            if self.user_response.lower().strip() == "b" or self.user_response.lower().strip() == "back":
                return self.receive_user_input()

            if self.user_response.lower().strip() == "q" or self.user_response.lower().strip() == "quit":
                exit()

            if not self.user_response.lower().title().strip() in item_classes:
                print("Please enter a valid command.")
                continue

            f = open("league_advisor/string_assets/items.json")
            data = json.load(f)
            data = data["data"]
            for i in data:
                recv_dt = data[i]["description"]
                if self.user_response.lower().title().strip() in recv_dt:
                    self.user_choise.append(data[i]["name"])
            f.close()

            if self.mode == "c":
                print()
                print(f"The item names below are in {color.GREEN}{self.user_response}{color.RESET} class.")
                user_choice = (",".join(self.user_choise).replace(',', " || ").replace(",", " "))
                print(f"{color.GREEN}{user_choice}{color.RESET}")
                print()

            else:
                print()
                print(f"The item names below are in {self.user_response} class.")
                print("*** Which item would you like to Preview? ***")
                print(",".join(self.user_choise).replace(',', " || ").replace(",", " "))
                print()

            item_names = []
            item_names = self.user_choise

        while not self.user_response.lower().title().strip() in self.user_choise:
            self.prompt_user()

            if self.user_response.lower().strip() == "b" or self.user_response.lower().strip() == "back":
                return self.receive_item()

            if self.user_response.lower().strip() == "q" or self.user_response.lower().strip() == "quit":
                exit()

            if not self.user_response.lower().strip() in [item.lower() for item in item_names]:
                print("Please enter a valid command.")
                continue
            
            f = open("league_advisor/string_assets/items.json")
            data = json.load(f)
            data = data["data"]
            for i in data:
                name_dt = data[i]["name"]
                if self.user_response.lower().strip() in name_dt.lower():
                    self.description = (data[i]["description"])
            f.close()

            if self.mode == "c":
                print()
                print(items_color_ascii.get(self.user_response.lower()))
                print(f"{color.GREEN}{self.user_response}{color.RESET}")
                print()

            else:
                print()
                print(items_ascii.get(self.user_response.lower()))
                print(f"{self.user_response}")
                print()

            description = re.sub(r"<[^>]*>","", self.description)

            if self.mode == "c":
                print(color.GREEN + description + color.RESET)
                print()

            else:
                print({description})
                print(self.user_response.lower())
                print()

    
            if self.mode == "c":
                print(f"To stop the program, enter ({color.RED}q{color.RESET})uit || ({color.RED}b{color.RESET})ack to the last menu.")   
                            
            else:
                print("To stop the program, enter (q)uit || (b)ack to the last menu.")
            self.user_choise = []


if __name__ == "__main__":
    leagueBrowser = LeagueBrowser()
    leagueBrowser.receive_user_input()



