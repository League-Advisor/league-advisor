"""This module tests InputHandler class methods"""

from league_advisor.input_handler import InputHandler 
from league_advisor.string_assets.menu_strings import strings
from tests.flo import diff
import pytest

def test_creates_instant(input_handler_fixture):
  #Arrange
  expected = ""

  #Act
  actual = input_handler_fixture.user_input

  #Assert
  assert actual == expected
  

def test_welcome_message(capfd):
  #Arrange  
  input_handler = InputHandler()
  input_handler.welcome_message()

  #Act
  out, err = capfd.readouterr()

  #Assert
  assert out == strings["logo_ascii"] + "\n" + strings["welcome_message"]+ "\n"
  assert err == ""

def test_help_user(capfd):
  #Arrange    
  input_handler = InputHandler()
  input_handler.help_user()

  #Act
  out, err = capfd.readouterr()

  #Assert
  assert out == strings["help_list"] + "\n"
  assert err == ""

def test_help_user_false(capfd):
  #Arrange 
  input_handler = InputHandler()
  input_handler.help_user()

  #Act
  out, err = capfd.readouterr()

  #Assert
  assert not out == "NOT FAIL"
  assert err == ""


def test_input_interpreter_help(capfd):
  #Arrange 
  input_handler = InputHandler()
  input_handler.user_input = "h"

  #Act
  input_handler.input_interpreter(input_handler.user_input)
  out, err = capfd.readouterr()

  #Assert
  assert out == strings["help_list"] + "\n"
  assert err == ""

def test_input_interpreter_false(capfd):
  #Arrange 
  input_handler = InputHandler()
  input_handler.user_input = "a"

  #Act
  input_handler.input_interpreter(input_handler.user_input)
  out, err = capfd.readouterr()

  #Assert
  assert not out == strings["help_list"] + "\n"
  assert err == ""

def test_input_interpreter_else(capfd):
  #Arrange 
  input_handler = InputHandler()
  input_handler.user_input = "else"

  #Act
  input_handler.input_interpreter(input_handler.user_input)
  out, err = capfd.readouterr()

  #Assert
  assert out == "Please enter a valid command." + "\n"
  assert err == ""

def test_input_interpreter_quit():
  #Arrange 
  input_handler = InputHandler()
  input_handler.user_input = "q"

  #Act
  with pytest.raises(SystemExit) as e:
    input_handler.input_interpreter(input_handler.user_input)

  #Assert
  assert e.type == SystemExit

def test_input_handler_welcome_screen(input_handler_fixture):
  diffs = diff(input_handler_fixture.welcome_message, path="tests/simulations/welcome_screen.sim.txt")
  assert not diffs, diffs

def test_input_handler_help_user(input_handler_fixture):

  diffs = diff(input_handler_fixture.help_user, path="tests/simulations/help_user.sim.txt")
  assert not diffs, diffs

def test_input_handler_color_mode(input_handler_fixture):

  diffs = diff(input_handler_fixture.color_mode, path="tests/simulations/color_mode.sim.txt")
  assert not diffs, diffs

@pytest.mark.skip("NEEDS SIMULATION")
def test_prompt_user():
  pass

# Fixtures
@pytest.fixture
def input_handler_fixture():
  input_handler = InputHandler()
  return input_handler
