"""This module will tests LeagueScraper class methodes"""
from league_advisor.league_scraper import LeagueScraper


def test_import_league_scraper():
    assert LeagueScraper()


def test_get_item_response():
    # Arrange
    league_scr = LeagueScraper()
    expected = 200
    # Actual
    actual = league_scr.get_item()
    # Assert
    assert actual == expected


# def test_get_champions_response():
#     # Arrange
#     league_scr = LeagueScraper()
#     expected = 200
#     # Actual
#     actual = league_scr.get_champion()
#     # Assert
#     assert actual == expected
