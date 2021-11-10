""" This module will preview the dataset that the user selected to browes"""

from league_advisor.string_assets.items import items_ascii
from league_advisor.string_assets.items_color import items_color_ascii
from league_advisor.string_assets.champs import champions_ascii
from league_advisor.string_assets.champs_color import champions_color_ascii
from league_advisor.string_assets.colors import color
import os
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

    def clear(self):
        clear = lambda: os.system('clear')
        clear()
    def receive_user_input(self):


        while True:
            if self.mode == "c":
                print()
                print(f"Would you like to preview ({color.RED}i{color.RESET})tems or ({color.RED}c{color.RESET})hampions?")
                print(f"To stop the program, enter ({color.RED}q{color.RESET})uit || ({color.RED}b{color.RESET})ack to the main menu.")            
            else:
                print()
                print("Would you like to preview (i)tems or (c)hampions?")
                print("To stop the program, enter (q)uit || (b)ack to the main menu.")
            self.prompt_user()
            self.clear()
            if self.user_response.lower().strip() == "i" or self.user_response.lower().strip() == "items":
                return self.receive_item()

            elif self.user_response.lower().strip() == "c" or self.user_response.lower().strip() == "champions":
                return self.receive_champions()

            elif self.user_response.lower().strip() == "b" or self.user_response.lower().strip() == "back":
                return self.user_response

            elif self.user_response.lower().strip() == "q" or self.user_response.lower().strip() == "quit":
                print("""
                    Thank you for using League Advisor. Hope to see you again soon!""")
                quit()

            else:
                print("Please enter a valid command.")

    def receive_item(self):
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
                self.clear()
                return self.receive_user_input()

            if self.user_response.lower().strip() == "q" or self.user_response.lower().strip() == "quit":
                print("""
                    Thank you for using League Advisor. Hope to see you again soon!""")
                quit()

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
                print(f"Items with {color.GREEN}{self.user_response}{color.RESET} stats.")
                user_choice = (",".join(self.user_choise).replace(',', " || ").replace(",", " "))
                print(f"{color.GREEN}{user_choice}{color.RESET}")
                print()

            else:
                print()
                print(f"Items with  {self.user_response} stats.")
                print("*** Which item would you like to Preview? ***")
                print(",".join(self.user_choise).replace(',', " || ").replace(",", " "))
                print()

            item_names = []
            item_names = self.user_choise

        while not self.user_response.lower().title().strip() in self.user_choise:
            self.prompt_user()

            if self.user_response.lower().strip() == "b" or self.user_response.lower().strip() == "back":
                self.clear()
                return self.receive_item()

            if self.user_response.lower().strip() == "q" or self.user_response.lower().strip() == "quit":
                print("""
                    Thank you for using League Advisor. Hope to see you again soon!""")
                quit()

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
                print(items_color_ascii.get(self.user_response.lower().strip()))
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
            

    def receive_champions(self):

        print(" Which champion tag would you like to check from the list below?")

        if self.mode == "c":
            print(f" To stop the program, enter ({color.RED}q{color.RESET})uit || ({color.RED}b{color.RESET})ack to the main menu.")

        else:
            print(" To stop the program, enter (q)uit || (b)ack to the main menu.")

        champion_tags = ["Fighter","Tank","Mage","Assassin","Marksman","Support"]

        champions = (",".join(champion_tags).replace('"', "").replace(",", " || "))

        if self.mode == "c":
            print(f"{color.GREEN}{champions}{color.RESET}")
            print()

        else:
            print(champions)
            print()

        while not self.user_response.lower().strip() in [tag.lower() for tag in champion_tags]:
            self.prompt_user()

            if self.user_response.lower().strip() == "b" or self.user_response.lower().strip()  == "back":
                self.clear()
                return self.receive_user_input()

            if self.user_response.lower().strip()  == "q" or self.user_response.lower().strip()  == "quit":
                exit()
            
            if not self.user_response.lower().strip() in [tag.lower() for tag in champion_tags]:
                print("Please enter a valid command.")
                continue
        
            else:
                with open("league_advisor/string_assets/champions.json") as f :
                    data = json.load(f)
                    data = data["data"]


                    for i in data:

                        if self.user_response.lower().strip() in [tag.lower() for tag in champion_tags]:
                            if self.user_response.lower().title().strip() in data[i]["tags"]:
                                self.user_choise.append(data[i]["name"])
                            
                   
                    champions_list = (",".join(self.user_choise).replace('"', "").replace(",", " || "))

                    if self.mode == "c":
                        print(f"{color.GREEN} {champions_list} {color.RESET}")
                        print()

                    else:
                        print(champions_list)
                        print()

                    print("Which champion whould you like to Know about?")

                self.prompt_user()

                if self.user_response.lower().strip() == "b" or self.user_response.lower().strip() == "back":
                    self.clear()
                    self.receive_champions()

                if self.user_response.lower().strip() == "q" or self.user_response.lower().strip() == "quit":
                    print("""
                        Thank you for using League Advisor. Hope to see you again soon!""")
                    quit()

            
                champion_info = []
                champion_figure = ""

                for i in data:
                    if self.user_response.lower().title().strip() in self.user_choise :
                        for key in champions_ascii:
                            if self.user_response.lower().strip() == key:

                                if self.mode == "c": 
                                    champion_figure = champions_color_ascii[key]

                                else:
                                    champion_figure = champions_ascii[key]

                        if self.user_response.lower().title().strip() == data[i]["name"]:
                                champion_info.append(data[i]["name"])
                                champion_info.append(data[i]["info"])
                                champion_info.append(data[i]["stats"])
                                champion_info.append(data[i]["blurb"])

            if self.mode == "c":
                print(f"""

            {champion_figure}

            {color.GREEN}{champion_info[3]}{color.RESET}

            {color.YELLOW}Champion name :{color.RESET} {color.CYAN}{champion_info[0]}{color.RESET}
            {color.YELLOW}Attack :{color.RESET} {color.CYAN}{champion_info[1]["attack"]} /10{color.RESET}
            {color.YELLOW}Defense :{color.RESET} {color.CYAN}{champion_info[1]["defense"]} /10{color.RESET}
            {color.YELLOW}Magic :{color.RESET} {color.CYAN}{champion_info[1]["magic"]} /10{color.RESET}
            {color.YELLOW}Difficulty :{color.RESET} {color.CYAN}{champion_info[1]["difficulty"]} /10{color.RESET}
            
            {color.YELLOW}Base Health :{color.RESET} {color.CYAN}{champion_info[2]["hp"]}{color.RESET}
            {color.YELLOW}Base Mana :{color.RESET} {color.CYAN}{champion_info[2]["mp"]}{color.RESET}
            {color.YELLOW}Base Armor :{color.RESET} {color.CYAN}{champion_info[2]["armor"]}{color.RESET}
            {color.YELLOW}Base Magic Resistance :{color.RESET} {color.CYAN}{champion_info[2]["spellblock"]}{color.RESET}
            {color.YELLOW}Attack Damage :{color.RESET} {color.CYAN}{champion_info[2]["attackdamage"]}{color.RESET}
            {color.YELLOW}Attack Range :{color.RESET} {color.CYAN}{champion_info[2]["attackrange"]}{color.RESET}
            {color.YELLOW}Attack Speed :{color.RESET} {color.CYAN}{champion_info[2]["attackspeed"]}{color.RESET}
            {color.YELLOW}Movement Speed :{color.RESET} {color.CYAN}{champion_info[2]["movespeed"]}{color.RESET}
                """)


            else:
                print(f"""

            {champion_figure}

            {champion_info[3]}

            Champion name : {champion_info[0]}
            Attack : {champion_info[1]["attack"]} /10
            Defense : {champion_info[1]["defense"]} /10
            Magic : {champion_info[1]["magic"]} /10
            Difficulty : {champion_info[1]["difficulty"]} /10
            
            Base Health : {champion_info[2]["hp"]}
            Base Mana : {champion_info[2]["mp"]}
            Base Armor : {champion_info[2]["armor"]}
            Base Magic Resistance : {champion_info[2]["spellblock"]}
            Attack Damage : {champion_info[2]["attackdamage"]}
            Attack Range : {champion_info[2]["attackrange"]}
            Attack Speed : {champion_info[2]["attackspeed"]}
            Movement Speed : {champion_info[2]["movespeed"]}
                 """)

            print("To go back to main menu , press any key")
            self.prompt_user()
            self.clear()
            return "b"


