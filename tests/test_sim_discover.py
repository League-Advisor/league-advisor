"""This module will tests LeagueBrowser class methodes"""

from league_advisor.discover import Discover
from tests.flo import diff

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
