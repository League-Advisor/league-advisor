""" This module analyze the data comes from match data scraper module"""
import pandas as pd
import json
from pandas.io.json import json_normalize
import difflib
from collections import Counter


class MatchData:
    """
    This class analyze the data comes from match data scraper module.

    Methods:

        data_analyzer : Direct his input to a data analysis model that elects the best possible candidate items for his situation
                        and return the items to the user
 
            Arguments: The user_input_list that comes from ranked_items

            Return: list of recoomended items
    """ 

    def __init__(self):
        self.user_input =[]
        self.champion = ''

    def data_analyzer(self,user_input) :
        self.user_input = user_input
        self.champion = user_input[2] 

        with open('league_advisor/string_assets/filtered_data_extra.json') as f:
            data = json.load(f)

        df = pd.json_normalize(data)

        df.to_csv('league_advisor/string_assets/match_data_analysis.csv', index=False)  

        champion_input=df[df.values == self.champion]
        
        champ_col = ''
        df_for_winners = pd.DataFrame()
        for i in champion_input.columns:
            helper_df = champion_input.loc[lambda champion_input: champion_input[i] == self.champion]
        
            if(not helper_df.empty):
                champ_col=i 
                for (j,row) in  helper_df.iterrows(): 
                        if "team1" in champ_col and row['team1.win'] :
                            df_for_winners = df_for_winners.append(row, ignore_index=True)
                     
                            
                        elif "team2" in champ_col and row['team2.win'] :
                            df_for_winners = df_for_winners.append(row, ignore_index=True)  
                      

                         
       
        teams_winners_list =[]

        for row in df_for_winners.itertuples():
        
            if row[1] == True :
                for i in range(2,11,2):
                
                    teams_winners_list.append(row[i])
                    
            if row[12] == True:
                for i in range(13,23,2):
                
                    teams_winners_list.append(row[i])    

        items_for_winners_list =[]

        for row in df_for_winners.itertuples():
            for i in range(23):
                if row[i] == self.champion:
            
                    items_for_winners_list.append(row[i+1])

        with open("league_advisor/string_assets/items.json" , "r") as f:
            items_names_list =[]
            data = json.load(f)
            data = data["data"]
            for i in range(len(items_for_winners_list)):
                for j in range(len(items_for_winners_list[i])):
                    string_item = str(items_for_winners_list[i][j])
                    if string_item in data :
                        items_names_list.append(data[string_item]["name"])
      
        recommended_build = []
        count_items=Counter(items_names_list)
        most_common_items_used=count_items.most_common()
        try:
            for i in range(5):
                recommended_build.append(most_common_items_used[i][0])
            return recommended_build
        except:
            print("There is no enough data , please try our solo champion")    
            return 