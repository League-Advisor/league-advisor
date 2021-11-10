"""This module simulates tests for solo_item class """

from league_advisor.league_advisor import LeagueAdvisor
from tests.flo import diff

def test_input_handler_solo_champion():
    league_advisor = LeagueAdvisor()  
    diffs = diff(league_advisor.run_program, path="tests/simulations/solo_champion.sim.txt")
    assert not diffs, diffs

def test_input_handler_help_browser_color():
    league_advisor = LeagueAdvisor()
    diffs = diff(league_advisor.run_program, path="tests/simulations/solo_champion_color.sim.txt")
    assert not diffs, diffs

def test_input_handler_solo_champion_back():
    league_advisor = LeagueAdvisor()  
    diffs = diff(league_advisor.run_program, path="tests/simulations/solo_champion_back.sim.txt")
    assert not diffs, diffs

def test_input_handler_solo_champion_back_color():
    league_advisor = LeagueAdvisor()  
    diffs = diff(league_advisor.run_program, path="tests/simulations/solo_champion_back_color.sim.txt")
    assert not diffs, diffs

def test_input_handler_solo_champion_quit():
    league_advisor = LeagueAdvisor()  
    diffs = diff(league_advisor.run_program, path="tests/simulations/solo_champion_quit.sim.txt")
    assert not diffs, diffs

def test_input_handler_solo_champion_quit_color():
    league_advisor = LeagueAdvisor()  
    diffs = diff(league_advisor.run_program, path="tests/simulations/solo_champion_quit_color.sim.txt")
    assert not diffs, diffs

def test_input_handler_solo_champion_error():
    league_advisor = LeagueAdvisor()  
    diffs = diff(league_advisor.run_program, path="tests/simulations/solo_champion_error.sim.txt")
    assert not diffs, diffs

def test_input_handler_solo_champion_error_color():
    league_advisor = LeagueAdvisor()  
    diffs = diff(league_advisor.run_program, path="tests/simulations/solo_champion_error_color.sim.txt")
    assert not diffs, diffs