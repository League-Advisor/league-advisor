# """ This module will scrape match data from RIOT API then format and filter it for data analysis
#     #NOTE: USE THIS MODULE ONLY FOR THE FIRST TIME YOU HAVE INSTALL THE PROGRAM OR IF YOU HAVE DELETED THE LOCAL DATA FILES
#     #NOTE: DON'T FORGET TO ADD YOUR RIOT API KEY IN .env FILE   
#     #NOTE: PLEASE BE CAREFUL NOT TO OVERWRITE ALREADY EXISTING DATA FILES WHEN TESTING THIS MODULE
#     #NOTE: TO USE THIS MODULE JUST UNCOMMENT THIS MODULE
# """

# import requests
# import json
# from dotenv import load_dotenv
# import os
# import time

# load_dotenv()
# api_key = os.environ.get("api_key")

# class MatchDataScraper:
#     """
#     This class scrapes match data, stores it locally in a JSON file as a list of dictionaries.

#     Methods:

#         match_scraper :

#             This methods sends a request for RIOT API server and stores the response in a json file locally.
#             Please add your RIOT API key to .env file as shown in .env.sample format.
            
#             Arguments: string, match_id

#             Return: None

#         -------------------------------------------------------------------------------------

#         get_match_data_by_id :

#             This method feeds match_scraper method with match IDs in an acceptable pace that is within the limits of API hit limits from Match IDs json file.
            
#             Arguments: None

#             Return: None


#         -------------------------------------------------------------------------------------

#         filter_match_data :

#             This method filters fetched data into a new lcoal JSON file.
            
#             Arguments: None

#             Return: None
        

#     """

#     def __init__(self):
#         self.flag = True
#         self.array = []
#         self.teams = {}

#     #NOTE: RUN THIS METHOD ONLY FOR THE FIRST TIME YOU HAVE INSTALL THE PROGRAM OR IF YOU HAVE DELETED THE LOCAL DATA FILES
#     def match_scraper(self, match_id):
#         request = requests.get(f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}")
#         if not request.status_code == 200:
#             request = requests.get(f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}")
#         if not request.status_code == 200:
#             request = requests.get(f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}")

#         print(request.status_code, match_id)

#         response = request.text        
#         res = json.loads(response)
#         if self.flag == True:
#             self.array.append(res)
#             self.flag = False
#             with open("league_advisor/string_assets/match.json", "w") as file:
#                 json.dump(self.array, file)

#         else:
#             if self.flag == False:
#                 with open("league_advisor/string_assets/match.json", mode='w') as f:
#                     self.array.append(res)
#                     json.dump(self.array, f)
#                     return

#     #NOTE: RUN THIS METHOD ONLY FOR THE FIRST TIME YOU HAVE INSTALL THE PROGRAM OR IF YOU HAVE DELETED THE LOCAL DATA FILES
#     def get_match_data_by_id(self):
#         with open("league_advisor/string_assets/games.json", "r") as file:
#             data = json.load(file)

#         for _ in range(1):
#             for _ in range(1):
#                 for id in data:
#                     self.match_scraper(id["match_id"])
#                     time.sleep(1)
#         return

#     #NOTE: RUN THIS METHOD ONLY FOR THE FIRST TIME YOU HAVE INSTALL THE PROGRAM OR IF YOU HAVE DELETED THE LOCAL DATA FILES
#     def filter_match_data(self):
#         with open("league_advisor/string_assets/match.json", "r") as file:
#             data = json.load(file)

#         with open("league_advisor/string_assets/filtered_data.json", "w") as file:
#             json.dump(self.array, file)

#         with open("league_advisor/string_assets/filtered_data.json", "w") as file:
#                 for match in data:
#                     try:
#                         champion_list = []
#                         team_items = []
#                         self.teams = {}
#                         for participant in match["info"]["participants"]:
#                             item_list = []
#                             for i in range(7):
#                                 item_list += [participant[f"item{i}"]] 
#                             champion_list.insert(0, participant["championName"])
#                             team_items.insert(0, item_list)
                            
#                         self.teams["team1"] = {
#                         "win" : match["info"]["teams"][0]["win"],
#                         "composition" : {
                                            
#                         "champion1": champion_list[0],
#                         "champion1_items" :team_items[0],

                        
#                         "champion2": champion_list[1],
#                         "champion2_items" :team_items[1],                             

                        
#                         "champion3": champion_list[2],
#                         "champion3_items" :team_items[2],       

                        
#                         "champion4": champion_list[3],
#                         "champion4_items" :team_items[3],       

                        
#                         "champion5": champion_list[4],
#                         "champion5_items" :team_items[4],                                                                                                                                   
#                         }
#                         }

#                         self.teams["team2"] = {
#                         "win" : match["info"]["teams"][1]["win"],
#                         "composition" : {
                                            
#                         "champion6": champion_list[5],
#                         "champion6_items" :team_items[5],

                        
#                         "champion7": champion_list[6],
#                         "champion7_items" :team_items[6],                             

                        
#                         "champion8": champion_list[7],
#                         "champion8_items" :team_items[7],       

                        
#                         "champion9": champion_list[8],
#                         "champion9_items" :team_items[8],       

                        
#                         "champion10": champion_list[9],
#                         "champion10_items" :team_items[9],                                                                                                                                   
#                         }
#                         }
#                         self.array.append(self.teams)

#                     except:
#                         print("An error occured, please clean your data and try again.")
#                         continue
                    
#                     json.dump(self.array, file)
            
                
# # if __name__ == '__main__':
#     # match = MatchDataScraper()
#     # match.filter_match_data()
#     # match.get_match_data_by_id()



