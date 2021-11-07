"""This module will scrape match data from RIOT API then format and filter it for data analysis"""

import requests
import json


class MatchDataScraper:
    """
    This class scrapes match data, stores it locally in a JSON file as a list of dictionaries.

        Methods:

            match_scraper
                Argument :
                    match_id : string

                Return: None

    """

    def __init__(self):
        self.flag = True
        self.array = []

    def match_scraper(self, match_id):
        flag = True
        request = requests.get(f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key=ENTER YOUR API KEY HERE")
        response = request.text
        # print(type(response))
        # print(type(res))

        
        res = json.loads(response)
        self.array.append(res)
        if self.flag == True:
            with open("league_advisor/string_assets/match.json", "w") as file:
                json.dump(self.array, file)
                self.flag = False

        if self.flag == False:
            with open("league_advisor/string_assets/match.json", mode='w') as f:
                self.array.append(res)
                json.dump(self.array, f)
                return


        

match = MatchDataScraper()
match.match_scraper("EUW1_5335612201")
match.match_scraper("EUW1_5411254491")

