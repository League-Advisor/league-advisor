"""This module tests Discover class methods"""
import pytest
from league_advisor.discover import Discover
from league_advisor.string_assets.menu_strings import strings

def test_import_class():
    #Assert
    assert Discover()

@pytest.mark.skip
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
    assert not out == strings["desc"] + "\n"
    assert err == ""  