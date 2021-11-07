""" This module will preview the dataset that the user selected to browes"""

import json


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
        print("Would you like to preview (i)tems or (c)hampions? (b)ack to go back to the main menu")
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
        print("*** Which class items would you like to check from the list above? ***\n")

        item_classes = ["Move Speed", "Base Mana Regen", "Base Health Regen", "Health", "Critical Strike Chance", "Ability Power", "Mana", "Armor", "Magic Resist",
                        "Omnivamp", "Attack Damage", "Attack Speed", "Life Steal", "Armor Penetration", "Lethality", "Ability Haste", "Physical Vamp", "Tenacity"]

        item_list = ["|| Move Speed ||", " Base Mana Regen ||", " Base Health Regen ||", " Health ||", " Critical Strike Chance ||", " Ability Power ||", " Mana ||", " Armor ||",
                     " Magic Resist ||", " Omnivamp ||", " Attack Damage ||", " Attack Speed ||", " Life Steal ||", " Armor Penetration ||", " Lethality ||", " Ability Haste ||", " Physical Vamp ||", " Tenacity ||"]

        print(",".join(item_list).replace('"', "").replace(",", ""))
        print()

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
                if self.user_response in recv_dt:
                    self.user_choise.append(data[i]["name"])

            print(self.user_choise)

            f.close()

    def receive_champions(self):
        print("champions_filter")


if __name__ == "__main__":
    leagueBrowser = LeagueBrowser()
    leagueBrowser.receive_user_input()
