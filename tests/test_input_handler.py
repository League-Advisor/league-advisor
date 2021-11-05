"""This module tests InputHandler class methods"""

from league_advisor.input_handler import InputHandler 
from league_advisor.string_assets.menu_strings import strings
import pytest

def test_creates_instant(input_handler_fixture):
  #Arrange
  expected = ""
  #Act
  actual = input_handler_fixture.user_input

  #Assert
  assert actual == expected
  


# Fixtures
@pytest.fixture
def input_handler_fixture():
  input_handler = InputHandler()
  return input_handler