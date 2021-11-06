"""This module interpets user input and redirects it to the corresponding function"""

from league_advisor.discover import Discover
from league_advisor.string_assets.menu_strings import strings



class InputHandler:
  """
  This class handles all user inputs and redirects them to their corresponding functions.

  Methods:

    welcome_message:

      Prints a welcoming message for the user and prompts them with the main menu.
      
      Arguments: None

      Return: None

    -------------------------------------------------------------------------------------

    prompt_user:

      Prompts user to enter his input and stores it.
      
      Arguments: None

      Return: None

    -------------------------------------------------------------------------------------

    quit_program:
      
      Prints a goodbye message then terminates the program.
      
      Arguments: None

      Return: None

    -------------------------------------------------------------------------------------


    help_user:

      Prints a string of all available commands and corresponding features to the user.
      
      Arguments: None

      Return: None

    -------------------------------------------------------------------------------------

    input_interpreter

      Redirects user input to invoke the corresponding function.
      
      Arguments: 
        user_input: string

      Return: None

  """

  def __init__(self):
    self.user_input = ""
    self.input_flag = False
 

  
  def welcome_message(self):
    print(strings["logo_ascii"])
    print(strings["welcome_message"])


  def prompt_user(self):
    self.user_input = input("> ")
    

  def quit_program(self):
    print("""
    Thank you for using League Advisor. Hope to see you again soon!""")
    quit()


  def help_user(self):
    print(strings["help_list"])

  def input_interpreter(self, user_input):

    if user_input.lower() == "h" or user_input.lower() == "help":
      self.help_user()

    elif user_input.lower() == "d" or user_input.lower() == "discover":
      dis =Discover()     
      dis.discover()

    elif user_input.lower() == "b" or user_input.lower() == "browse":
      self.input_flag = True
      print("browse")

    elif user_input.lower() == "s" or user_input.lower() == "solo":
      self.input_flag = True
      print("solo")

    elif user_input.lower() == "r" or user_input.lower() == "ranked":
      self.input_flag = True
      print("ranked")

    elif user_input == "q" or user_input.lower() == "quit":
      self.quit_program()

    else:
      print("Please enter a valid command.")


# a=InputHandler()
# b=a.prompt_user()
# a.input_interpreter(b)
