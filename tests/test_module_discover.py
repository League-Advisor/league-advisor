"""This module tests Discover class methods"""

from league_advisor.discover import Discover

def test_import_class():
    #Assert
    assert Discover()


def test_get_color_mode():
    #Arrange
    discover = Discover()
    discover.mode="c"
    expected = discover.mode

    #Act
    actual=discover.get_color_mode("c")

    #Assert
    assert expected == actual

  

