"""This module will tests MatchData class methodes"""
from league_advisor.match_data_analysis import MatchData

def test_create_instance():
    #Assert
    assert MatchData()

def test_data_analyzer_one():
    #Arrange
    user_input=[["Nami", "Ashe", "Ryze", "Nidalee", "Yone"],["Blitzcranck", "Aphelios", "Syndra", "Sejuan", "Gnar"],"Yone"]
    recommended_build= MatchData()
    expected=["Berserker's Greaves", 'Immortal Shieldbow', 'Stealth Ward', 'Infinity Edge', "Doran's Blade"]

    #Act
    actual=recommended_build.data_analyzer(user_input)

    #Assert
    assert actual == expected

def test_data_analyzer_no_items():
    #Arrange
    user_input=[["ahri", "irelia", "Ryze", "akshan", "aatrox"],["Tryndamere", "Samira", "teemo", "Sejuan", "Gnar"],"teemo"]      
    recommended_build= MatchData()
    expected = "There is no enough data , please try our solo champion"

    #Act
    actual=recommended_build.data_analyzer(user_input)

    #Assert
    assert actual == expected    
