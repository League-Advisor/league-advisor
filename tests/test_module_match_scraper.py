# """ This module will tests MatchDataScraper class methodes
#     #NOTE: USE THIS TEST MODULE ONLY AFTER YOU VIEW (match_data_scraper) MODUL
#     #NOTE: DON'T FORGET TO ADD YOUR RIOT API KEY IN .env FILE   
#     #NOTE: PLEASE BE CAREFUL NOT TO OVERWRITE ALREADY EXISTING DATA FILES
# """

# from league_advisor.match_data_scraper import MatchDataScraper
# from dotenv import load_dotenv
# import os
# import pytest

# load_dotenv()
# api_key = os.environ.get("api_key")

# @pytest.mark.skip
# def test_match_scraper(match_data_scraper):
#     #Arrange
#     expected = None 
#     #Act
#     match_data_scraper.match_scraper("EUW1_5409338400")

#     #Assert
#     assert expected ==  None

# @pytest.mark.skip
# def test_filter_match_data(match_data_scraper):
#     #Arrange
#     expected = None 
#     #Act
#     match_data_scraper.filter_match_data()

#     #Assert
#     assert expected ==  None

# @pytest.mark.skip
# def test_get_match_data_by_id(match_data_scraper):
#     #Arrange
#     expected = None 
#     #Act
#     match_data_scraper.get_match_data_by_id()

#     #Assert
#     assert expected ==  None


# @pytest.fixture
# def match_data_scraper():
#     match_data_scraper = MatchDataScraper()
#     return match_data_scraper