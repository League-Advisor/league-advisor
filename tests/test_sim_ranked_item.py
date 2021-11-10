from league_advisor.league_advisor import LeagueAdvisor
from tests.flo import diff


def test_ranked_item_error():
    league_advisor = LeagueAdvisor()
    diffs = diff(league_advisor.run_program,
                 path="tests/simulations/ranked_error_color.sim.txt")
    assert not diffs, diffs


def test_ranked_item_passed():
    league_advisor = LeagueAdvisor()
    diffs = diff(league_advisor.run_program,
                 path="tests/simulations/ranked_item_color_r.sim.txt")
    assert not diffs, diffs
