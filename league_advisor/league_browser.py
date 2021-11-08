""" This module will preview the dataset that the user selected to browes"""

from league_advisor.string_assets.items import items_ascii
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

        Redirects user input to invoke the corresponding function..

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

    def prompt_user(self):
        self.user_response = input("> ")

    def receive_user_input(self):
        print()
        print("Would you like to preview (i)tems or (c)hampions?")
        print("To stop the program, enter (q)uit || (b)ack to the main menu.\n")
        while True:
            self.prompt_user()
            if self.user_response.lower() == "i" or self.user_response.lower() == "items":
                return self.receive_item()

            elif self.user_response.lower() == "c" or self.user_response.lower() == "champions":
                return self.receive_champions()

            elif self.user_response.lower() == "b" or self.user_response.lower() == "back":
                return self.user_response

            elif self.user_response.lower() == "q" or self.user_response.lower() == "quit":
                exit()
            else:
                print("Please enter a valid command.")

    def receive_item(self):

        print()
        print("*** Which class items would you like to check from the list below? ***\n")
        print("To stop the program, enter (q)uit || (b)ack to the main menu.")
        print()

        item_classes = ["Move Speed", "Base Mana Regen", "Base Health Regen", "Health", "Critical Strike Chance", "Ability Power", "Mana", "Armor", "Magic Resist",
                        "Omnivamp", "Attack Damage", "Attack Speed", "Life Steal", "Armor Penetration", "Lethality", "Ability Haste", "Physical Vamp", "Tenacity"]

        print(",".join(item_classes).replace(',', " || ").replace(",", " "))
        print()
        print("To stop the program, enter (q)uit || (b)ack to the last menu.\n")

        while not self.user_response.lower().title() in item_classes:
            self.prompt_user()

            if self.user_response.lower() == "b" or self.user_response.lower() == "back":
                return self.receive_user_input()

            if self.user_response.lower() == "q" or self.user_response.lower() == "quit":
                exit()

            if not self.user_response.lower().title() in item_classes:
                print("Please enter a valid command.")
                continue

            f = open("league_advisor/string_assets/items.json")
            data = json.load(f)
            data = data["data"]
            for i in data:
                recv_dt = data[i]["description"]
                if self.user_response.lower().title() in recv_dt:
                    self.user_choise.append(data[i]["name"])
            f.close()
            print()
            print(f"The item names below are in {self.user_response} class.")
            print()
            print(",".join(self.user_choise).replace(',', " || ").replace(",", " "),"\n")
            print("To stop the program, enter (q)uit || (b)ack to the last menu.\n")
            item_names = []
            item_names = self.user_choise
#/////////////////////////////////////
        print()
        print("*** Which item would you like to Preview from the list above? ***\n")
        print("To stop the program, enter (q)uit || (b)ack to the last menu.\n")
        print()

        while not self.user_response.lower().title() in self.user_choise:
            self.prompt_user()

            if self.user_response.lower() == "b" or self.user_response.lower() == "back":
                return self.receive_item()

            if self.user_response.lower() == "q" or self.user_response.lower() == "quit":
                exit()

            if not self.user_response.lower() in [item.lower() for item in item_names]:
                print("Please enter a valid command.\n")
                continue
            
            f = open("league_advisor/string_assets/items.json")
            data = json.load(f)
            data = data["data"]
            for i in data:
                name_dt = data[i]["name"]
                if self.user_response.lower().title() in name_dt:
                    self.user_choise = []
                    self.user_choise.append(data[i]["description"])
            f.close()

            print()
            print(f"The description below is for {self.user_response} item.\n")
            print(items_ascii.get(self.user_response.lower()))
            match = re.sub(r"(?=)<+[a-z][A-z]+>", "","".join(self.user_choise))
            match_1 = re.sub(r"</+(?=)+[a-z][A-z]+>", "", match)
            match_2 = re.findall(r"(?=) [ ^A[A-z\d+%]*]*",  match_1)
            for i in match_2:
                print("*** {}  ~~-\/||\/-~~\n".format(i))
            print("To stop the program, enter (q)uit || (b)ack to the last menu.\n")
            self.user_choise = []
            

    # def receive_champions(self):
    #     print("champions_filter")


if __name__ == "__main__":
    leagueBrowser = LeagueBrowser()
    leagueBrowser.receive_user_input()
