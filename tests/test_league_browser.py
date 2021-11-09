"""This module will tests LeagueBrowser class methodes"""

from league_advisor.league_browser import LeagueBrowser
from tests.flo import diff

def test_import_class():
    assert LeagueBrowser()


def test_leaguebrowser_receive_user_input_method_quit():
    leaguebrowser = LeagueBrowser()
    diffs = diff(leaguebrowser.receive_user_input,path="tests/simulations/leaguebrowser_receive_user_input_method_quit.sim.txt")
    assert not diffs, diffs


def test_leaguebrowser_receive_user_input_method_item_class():
    leaguebrowser = LeagueBrowser()
    diffs = diff(leaguebrowser.receive_user_input, path="tests/simulations/leaguebrowser_receive_user_input_method_item.sim.txt")
    assert not diffs, diffs

#
def test_leaguebrowser_receive_item_method_classes():
    leaguebrowser = LeagueBrowser()
    diffs = diff(leaguebrowser.receive_user_input, path="tests/simulations/leaguebrowser_receive_item_method_classes.sim.txt")
    assert not diffs, diffs


def test_leaguebrowser_receive_item_method_names():
    leaguebrowser = LeagueBrowser()
    diffs = diff(leaguebrowser.receive_user_input, path="tests/simulations/leaguebrowser_receive_item_method_names.sim.txt")
    assert not diffs, diffs

#
def test_leaguebrowser_receive_item_method_names_backmenu():
    leaguebrowser = LeagueBrowser()
    diffs = diff(leaguebrowser.receive_user_input,
                 path="tests/simulations/leaguebrowser_receive_item_method_classes_backmenu.sim.txt")
    assert not diffs, diffs


def test_leaguebrowser_receive_item_method_classes_backmenu():
    leaguebrowser = LeagueBrowser()
    diffs = diff(leaguebrowser.receive_user_input,
                 path="tests/simulations/leaguebrowser_quetter.sim.txt")
    assert not diffs, diffs

