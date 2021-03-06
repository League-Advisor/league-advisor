"""This module tests solo_item class """

from league_advisor.solo_items import SoloItems


def test_solo_item_get_items_lucian():
    # Arrange
    item = SoloItems()
    expected = ["Doran's Blade", 'Kraken Slayer', "Berserker's Greaves",
                'Essence Reaver', 'Navori Quickblades', 'Infinity Edge']
    # Act
    actual = item.get_items("lucian")
    # Assert
    assert expected == actual


def test_solo_item_get_items_zed():
    # Arrange
    item = SoloItems()
    expected = ['Long Sword', 'Duskblade of Draktharr', "Mercury's Treads",
                "Youmuu's Ghostblade", 'Black Cleaver', 'Edge of Night', "Serylda's Grudge"]
    # Act
    actual = item.get_items("zed")
    # Assert
    assert expected == actual

def test_solo_clear():
    # Arrange
    solo_item = SoloItems()
    expected = None

    # Act
    actual = solo_item.clear()

    # Assert
    assert expected == actual
   
def test_color_mode():
    # Arrange
    solo_item = SoloItems()
    expected = "c"

    #Act
    actual = solo_item.get_color_mode("c")

    # Assert
    assert actual == expected 

