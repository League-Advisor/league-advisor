"""This module provides a class to print colored strings to the terminal """

class color:
  """
  This class provides coloration for printed string 

  Methods: None
  Arguments: None
  Return: None
  """
  RED   = "\033[1;31m"  
  BLUE  = "\033[1;34m"
  CYAN  = "\033[1;36m"
  GREEN = "\033[0;32m"
  RESET = "\033[0;0m"
  BOLD    = "\033[;1m"
  REVERSE = "\033[;7m"