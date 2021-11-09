"""This module provides a class to print colored strings to the terminal """

class color:
  """
  This class provides coloration for printed string 

  Methods: None
  Arguments: None
  Return: None
  """
  BLACK = "\033[1;30m"
  RED   = "\033[1;31m"  
  GREEN = "\033[1;32m"
  BLUE  = "\033[1;34m"
  MAGENTA = "\033[1;35m"
  CYAN  = "\033[1;36m"
  WHITE = "\033[1;37m"
  YELLOW = "\033[1;33m"
  BOLD    = "\033[;1m"
  REVERSE = "\033[;7m"
  RESET = "\033[0;0m"

  BLACK_BG = "\033[1;40m"
  RED_BG = "\033[1;41m"
  GREEN_BG = "\033[1;42m"
  YELLOW_BG = "\033[1;43m"
  BLUE_BG = "\033[1;44m"
  MAGENTA_BG = "\033[1;45m"
  CYAN_BG = "\033[1;46m"
  WHITE_BG = "\033[1;47m"
  RESET_BG = "\033[1;49m"

