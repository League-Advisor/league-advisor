"""This module will tests recieve champion method in LeagueBrowser class"""

import pytest
from league_advisor.league_browser import LeagueBrowser

def test_recieve_champion_tags(capfd):
    #Arrange 
    champion = LeagueBrowser()
   
    #Act
    champion.user_response = "Fighter"
    champion.receive_champions()
    out, err = capfd.readouterr()

    #Assert

    assert out == """*** Which champion tag would you like to check from the list above? ***
        To go (b)ack    
        
Fighter || Tank || Mage || Assassin || Marksman || Support"""+"\n"+"\n"
    assert err == ""  

