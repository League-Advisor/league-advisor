"""This module tests Discover class methods"""

from league_advisor.discover import Discover
from league_advisor.string_assets.menu_strings import strings
from tests.flo import diff

def test_import_class():
    #Assert
    assert Discover()


def test_discover_method():
    discover = Discover()
    diffs = diff(discover.discover,path="tests/simulations/discover_method.sim.txt")
    assert not diffs, diffs

def test_discover_method_quit():
    discover = Discover()
    diffs = diff(discover.discover,path="tests/simulations/discover_method_quit.txt")
    assert not diffs, diffs

def test_discover_method_any_key():
    discover = Discover()
    diffs = diff(discover.discover,path="tests/simulations/discover_method_any_key.txt")
    assert not diffs, diffs

def test_get_color_mode():
    #Arrange
    discover = Discover()
    discover.mode="c"
    expected = discover.mode

    #Act
    actual=discover.get_color_mode("c")

    #Assert
    assert expected == actual

  

