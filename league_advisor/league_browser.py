""" This module will preview the dataset that the user selected to browes"""

import json
from league_advisor.string_assets.menu_strings import strings

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
            return self.user_choise

    def receive_champions(self):
        
        print("""*** Which champion tag would you like to check from the list above? ***
        To go (b)ack    
        """)

        champion_tags = ["Fighter","Tank","Mage","Assassin","Marksman","Support"]

        print(",".join(champion_tags).replace('"', "").replace(",", " || "))
        print()

        while not self.user_response.lower().title() in champion_tags:
            self.prompt_user()

            if self.user_response.lower() == "b" or self.user_response.lower() == "back":
                return self.receive_user_input()

            if self.user_response.lower() == "q" or self.user_response.lower() == "quit":
                exit()
            
            if not self.user_response.lower().title() in champion_tags:
                print("Please enter a valid command.")
                continue
        
            else:
                with open("league_advisor/string_assets/champions.json") as f :
                    data = json.load(f)
                    data = data["data"]


                    for i in data:

                        if self.user_response.lower().title() in champion_tags:
                            if self.user_response.lower().title() in data[i]["tags"]:
                                self.user_choise.append(data[i]["name"])
                            
                   
                    print(",".join(self.user_choise).replace('"', "").replace(",", " || "))
                    print()
                    print("""
                    Which champion whould you like to Know about?
                    To go (b)ack 
                    """)
                if self.user_response.lower() == "b" or self.user_response.lower() == "back":
                    self.receive_champions()
                # else :    
                self.prompt_user()

                if self.user_response.lower() == "b" or self.user_response.lower() == "back":
                    self.receive_champions()

            champion_info = []
            for i in data:
                if self.user_response.lower().title() in self.user_choise :
                    if self.user_response.lower().title() == data[i]["name"]:
                            champion_info.append(data[i]["name"])
                            champion_info.append(data[i]["info"])
                            print(f"""
                            Champion name : {champion_info[0]}
                            Attack : {champion_info[1]["attack"]}
                            Defense : {champion_info[1]["defense"]}
                            Magic : {champion_info[1]["magic"]}
                            Difficulty : {champion_info[1]["difficulty"]}
                            """)
                            print("To go back to main menu , press any key")
                            self.prompt_user()
                            return "b"




if __name__ == "__main__":
    leagueBrowser = LeagueBrowser()
    leagueBrowser.receive_user_input()
