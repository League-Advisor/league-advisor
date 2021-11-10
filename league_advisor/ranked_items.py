"""This module will get user choice and comapre it with the list of champions and then send it to data analysis module to pick the optimal items for the user with respect to user team champions also with respect to enemy team champions"""

from league_advisor.string_assets.menu_strings import strings


class RankedItem:
    """This module will direct the user input to the match data analysis module

     Methods:
    ---

      prompt_user:

      this method will ask the user to input names of champion separting them with comma

      Arguments: None

      Return: None
    ---

      handle_user_choice:

        this method will check if the user input champion are exists in the list of champions 

        Arguments: None

        Return: weather if the user input real names of champions or not 
    ---    
      handle_user_input:

        this method will check if the user input five names or not  

        Arguments: None

        Return: weather if the user input 5 names seperated by comma or not  
    ---    
      prompt_user_enemy:

        this method will ask the user to input names of champion of enemy team separting them with comma

        Arguments: None

        Return: weather if the user input 5 names seperated by comma or not
    ---

      handle_enemy_choice:

         this method will check if the user input five names or not  

        Arguments: None

        Return: weather if the user input 5 names seperated by comma or not 
    ---
      handle_user_enemy:

        this method will check if the user input five names or not  

        Arguments: None

        Return: weather if the user input 5 names seperated by comma or not  
    ---
      handle_match:

        this method will check if the user input any champion name in both team or not   

        Arguments: None

        Return: weather if the user input a name of champion in both team or not and if true it well ask him to modefiy the enemy team and if not it will return a list of champion names                        
    """

    def __init__(self):
        self.user = []
        self.match = []
        self.user_champion = ""
        self.enemy_champion = ""
        self.user_flage = False
        self.enemy_flage = False
        self.mode = ""

    def get_color_mode(self, color_mode):
        self.mode = color_mode
        return self.mode     

    def prompt_user(self):
       
            print("Enter your team champion seperated by comma, starting with your champion name.")
            self.user_champion = input("> ")
        
    def handle_user_choice(self):

        for champ in self.user[0]:
            if champ.lower().strip() in strings["champion_list_lower"]:
                champ = champ.title()
                self.user_flage = True

            else:
                print("You entered wrong names")
                self.handle_user_input()
        if self.user_flage == True:
            self.match.insert(0, self.user_champion.split(","))
            self.handle_user_enemy()

    def handle_user_input(self):

        self.prompt_user()
        if self.user_champion == "b":
            return
        self.user.insert(0, self.user_champion.split(","))
        if len(set(self.user[0])) == 5:
            self.handle_user_choice()
        else:
            print("You should add 5 unique champion names")
            self.handle_user_input()

    def prompt_user_enemy(self):
        print("Enter your enemy team champions seperated by comma.")
        self.enemy_champion = input("> ")

    def handle_enemy_choice(self):
        for champ in self.user[1]:
            if champ.lower().strip() in strings["champion_list_lower"]:
                self.enemy_flage = True
                champ = champ.title()
            else:
                print("You entered wrong enemy names")
                self.handle_user_enemy()
        if self.enemy_flage == True:
            self.match.insert(1, self.enemy_champion.split(","))
            self.handle_match()
            
    def handle_user_enemy(self):

        self.prompt_user_enemy()
        if self.enemy_champion == "b":
            return
        self.user.insert(1, self.enemy_champion.split(","))
        if len(set(self.user[1])) == 5:
            self.handle_enemy_choice()
        else:
            print("You should add 5 enemy unique champion names")
            self.handle_user_enemy()

    def handle_match(self):
        for i in self.match[0]:
            for j in self.match[1]:
                if i == j:
                    print("Same champion can not be in both team ")
                    self.match.pop(1)

                    self.handle_user_enemy()
                    self.match.pop(2)

        self.match.append(self.match[0][0])
        for i in self.match[0]:
            i=i.title()
        for j in self.match[1]:
           j = j.title()
        self.match[2] = self.match[2].title()
          
        return self.match
