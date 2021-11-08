"""This module will get user choice and comapre it with the list of champions and then send it to data analysis module to pick the optimal items for the user with respect to user team champions also with respect to enemy team champions"""

from league_advisor.string_assets.champions import champy


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
    """

    def __init__(self):
        self.user = []
        self.champion = ""
        self.correct_flage = False

    def prompt_user(self):
        print("Enter your team champion seperated by comma")
        self.champion = input("> ")

    def handle_user_choice(self):
        # print(self.user[0])
        for champ in self.user[0]:
            if champ in champy:
                self.correct_flage = True

            if champ not in champy:
                print("You entered wrong names")
                self.handle_user_input()
        if self.correct_flage == True:
            print("you entered correct name")

    def handle_user_input(self):

        self.prompt_user()
        self.user.insert(0, self.champion.split(","))
        if len(set(self.user[0])) == 5:
            print("You entered 5 champions")
            self.handle_user_choice()
        else:
            print("You should add 5 unique champion names")
            self.handle_user_input()
