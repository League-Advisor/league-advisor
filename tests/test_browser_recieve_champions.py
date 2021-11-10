"""This module will tests LeagueBrowser class methodes"""

from league_advisor.league_browser import LeagueBrowser
from tests.flo import diff

def test_import_class():
    assert LeagueBrowser()


def test_leaguebrowser_receive_champions_start():
    leaguebrowser = LeagueBrowser()
    diffs = diff(leaguebrowser.receive_champions,path="tests/simulations/browser_recieve_champions_start.sim.txt")
    assert not diffs, diffs

def test_leaguebrowser_receive_champions_info():
    leaguebrowser = LeagueBrowser()
    diffs = diff(leaguebrowser.receive_champions,path="tests/simulations/browser_recieve_champions_info.sim.txt")
    assert not diffs, diffs    