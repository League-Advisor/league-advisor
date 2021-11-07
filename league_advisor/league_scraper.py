""" This module will scrapes the latest version of items and stats"""
import requests


class LeagueScraper:
    """This class will scrapes the latest version of items and stats then store them in json files ".

    Methods:
    ---

      get_item:

        Scrapes items data from ddragon.leagueoflegends.com then save the response in json file.

        Arguments: None

        Return:  response status_code

    ---

      get_champion:

        Scrapes champions data from ddragon.leagueoflegends.com then save the response in json file.

        Arguments: None

        Return: response status_code
    """

    def __init__(self):
        self.items = "http://ddragon.leagueoflegends.com/cdn/11.22.1/data/en_US/item.json"
        self.champions = "http://ddragon.leagueoflegends.com/cdn/11.22.1/data/en_US/champion.json"

    def get_item(self):
        items = requests.get(self.items)
        response = items.text
        with open("league_advisor/string_assets/items.json", "w+") as f:
            f.write(response)
        return items.status_code

    def get_champion(self):
        champions = requests.get(self.champions)
        response = champions.text
        with open("league_advisor/string_assets/champions.json", "w+") as f:
            f.write(response)
        return champions.status_code


if __name__ == '__main__':
    leag_csrp = LeagueScraper()
    print(leag_csrp.get_item())
    print(leag_csrp.get_champion())
