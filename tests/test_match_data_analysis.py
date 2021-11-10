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
    expected = None

    #Act
    actual=recommended_build.data_analyzer(user_input)

    #Assert
    assert actual == expected


def test_data_analyzer_items():
    #Arrange
    user_input = [["Ezreal",  "Nami",  "Syndra", "Nidalee", "Yone"], [
        "Blitzcranck", "Lillia", "Jax", "Sejuan", "Morgana"], "Ezreal"]
    recommended_build= MatchData()
    expected = ['Ionian Boots of Lucidity', 'Farsight Alteration',
                'Divine Sunderer', 'Muramana', "Doran's Blade"]
    #Act
    actual=recommended_build.data_analyzer(user_input)
    assert actual == expected
