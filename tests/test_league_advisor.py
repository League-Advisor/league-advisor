"""This module tests LeagueAdvisor class methods"""

from league_advisor.league_advisor import LeagueAdvisor
from tests.flo import diff

def test_quit_welcome_massage():
    leagueadvisor = LeagueAdvisor()
    diffs = diff(leagueadvisor.run_program, path="tests/quetter.sim.txt")
    assert not diffs, diffs


def test_helper_docs_():
    leagueadvisor = LeagueAdvisor()
    diffs = diff(leagueadvisor.run_program, path="tests/helper.sim.txt")
    assert not diffs, diffs


def test_discover_roles_docs_():
    leagueadvisor = LeagueAdvisor()
    diffs = diff(leagueadvisor.run_program, path="tests/discover.sim.txt")
    assert not diffs, diffs


def test_discover_menu_back_docs_():
    leagueadvisor = LeagueAdvisor()
    diffs = diff(leagueadvisor.run_program, path="tests/discover_menu_back.sim.txt")
    assert not diffs, diffs


def test_prowser_docs_():
    leagueadvisor = LeagueAdvisor()
    diffs = diff(leagueadvisor.run_program, path="tests/prowser.sim.txt")
    assert not diffs, diffs


def test_prowser_menu_back_():
    leagueadvisor = LeagueAdvisor()
    diffs = diff(leagueadvisor.run_program, path="tests/prowser.sim.txt")
    assert not diffs, diffs


# def test_prowser_menu_quit_():
#     leagueadvisor = LeagueAdvisor()
#     diffs = diff(leagueadvisor.run_program, path="tests/prowser_menu_quit.sim.txt")
#     assert not diffs, diffs


# def test_prowser_items_class_():
#     leagueadvisor = LeagueAdvisor()
#     diffs = diff(leagueadvisor.run_program, path="tests/prowser_item_class.sim.txt")
#     assert not diffs, diffs


# def test_prowser_items_menu_():
#     leagueadvisor = LeagueAdvisor()
#     diffs = diff(leagueadvisor.run_program, path="tests/browser_item_menu.sim.txt")
#     assert not diffs, diffs
