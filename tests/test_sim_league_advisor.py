"""This module tests LeagueAdvisor class methods"""

from league_advisor.league_advisor import LeagueAdvisor
from tests.flo import diff

def test_input_handler_help_user_color():
  league_advisor = LeagueAdvisor()
  diffs = diff(league_advisor.run_program, path="tests/simulations/help_color.sim.txt")
  assert not diffs, diffs

def test_input_handler_help_solo_color():
    league_advisor = LeagueAdvisor()
    diffs = diff(league_advisor.run_program, path="tests/simulations/solo_champion_color.sim.txt")
    assert not diffs, diffs

