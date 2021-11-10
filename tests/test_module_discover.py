"""This module tests Discover class methods"""

from league_advisor.discover import Discover
from league_advisor.string_assets.menu_strings import strings

def test_import_class():
    #Assert
    assert Discover()


def test_discover_method(capfd):
    """
    Interactive test
    """
    #Arrange 
    discover = Discover()

    #Act
    discover.discover()
    out, err = capfd.readouterr()

    #Assert
    assert not out == strings["disc"] + "\n"
    assert err == ""  