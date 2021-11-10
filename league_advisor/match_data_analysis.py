""" This module analyze the data comes from match data scraper module"""
import pandas as pd
import json
# from pandas.io.json import json_normalize
import difflib as diff
from collections import Counter


class MatchData:
    """
    This class analyze the data comes from match data scraper module.

    Methods:

        data_analyzer : Direct his input to a data analysis model that return items are commonly bought elects the best possible candidate items for his situation
                        and return the items to the user
 
            Arguments: The user_input_list that comes from ranked_items

            Return: list of items are commonly bought recoomended items

        data_analyzer_items : Direct his input to a data analysis model that elects the best possible candidate items for his situation
                        and return the items to the user
 
            Arguments: The user_input_list that comes from ranked_items

            Return: list of recoomended items
    """ 

    def __init__(self ):
        self.user_input =[]
        self.champion = ''
        self.df_for_winners = []
    def data_analyzer(self,user_input) :
        self.user_input = user_input
        self.champion = user_input[2] 

        with open('league_advisor/string_assets/filtered_data_extra.json') as f:
            data = json.load(f)

        df = pd.json_normalize(data)

        df.to_csv('league_advisor/string_assets/match_data_analysis.csv', index=False)  

        champion_input=df[df.values == self.champion]
        
        champ_col = ''
        self.df_for_winners = pd.DataFrame()
        for i in champion_input.columns:
            helper_df = champion_input.loc[lambda champion_input: champion_input[i] == self.champion]
        
            if(not helper_df.empty):
                champ_col=i 
                for (j,row) in  helper_df.iterrows(): 
                        if "team1" in champ_col and row['team1.win'] :
                            self.df_for_winners = self.df_for_winners.append(row, ignore_index=True)
                     
                            
                        elif "team2" in champ_col and row['team2.win'] :
                            self.df_for_winners = self.df_for_winners.append(row, ignore_index=True)  
        

        teams_winners_list =[]

        for row in self.df_for_winners.itertuples():
        
            if row[1] == True :
                for i in range(2,11,2):
                
                    teams_winners_list.append(row[i])
                    
            if row[12] == True:
                for i in range(13,23,2):
                
                    teams_winners_list.append(row[i])    

        items_for_winners_list =[]

        for row in self.df_for_winners.itertuples():
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
            return f"These items are commonly bought for your champion: ==> {recommended_build}"
        except:
            print("There is no enough data , please try our solo champion")    
            
        

    def data_analyzer_items(self):

        self.user_team = self.user_input[0]
        team_1_champions_winer = []
        team_2_champions_winer = []
        winer_items = []
        champion = self.champion

        for index, row in self.df_for_winners.iterrows():
            team_1_champions_winer.append(row["team1.composition.champion1"])
            team_1_champions_winer.append(row["team1.composition.champion2"])
            team_1_champions_winer.append(row["team1.composition.champion3"])
            team_1_champions_winer.append(row["team1.composition.champion4"])
            team_1_champions_winer.append(row["team1.composition.champion5"])

            if row['team1.win'] == True and champion in team_1_champions_winer:
                team_1_champions_winer = []
                team_1_champions_winer.append(index)
                team_1_champions_winer.append(row["team1.composition.champion1"])
                team_1_champions_winer.append(row["team1.composition.champion2"])
                team_1_champions_winer.append(row["team1.composition.champion3"])
                team_1_champions_winer.append(row["team1.composition.champion4"])
                team_1_champions_winer.append(row["team1.composition.champion5"])

                winer_items.append(team_1_champions_winer)
                team_1_champions_winer = []

        #/////////////////////////////////////////////////////////////////////////////#

            team_2_champions_winer.append(row["team2.composition.champion6"])
            team_2_champions_winer.append(row["team2.composition.champion7"])
            team_2_champions_winer.append(row["team2.composition.champion8"])
            team_2_champions_winer.append(row["team2.composition.champion9"])
            team_2_champions_winer.append(row["team2.composition.champion10"])

            if row['team2.win'] == True and champion in team_2_champions_winer:
                team_2_champions_winer = []
                team_2_champions_winer.append(index)
                team_2_champions_winer.append(row["team2.composition.champion6"])
                team_2_champions_winer.append(row["team2.composition.champion7"])
                team_2_champions_winer.append(row["team2.composition.champion8"])
                team_2_champions_winer.append(row["team2.composition.champion9"])
                team_2_champions_winer.append(row["team2.composition.champion10"])

                winer_items.append(team_2_champions_winer)
                team_2_champions_winer = []
        # print(winer_items)

        threshold = 0.40
        data_normalyzed_str = ""
        data_normalyzed_items = []
        for i in winer_items:
            sm = diff.SequenceMatcher(None, i, self.user_team)
            ratio = sm.ratio()
            if ratio > threshold:
                idx = (i[0])
                for index, row in self.df_for_winners.iterrows():
                    if index == idx:
                        col_name = row.iloc[row.values == self.champion]
                        col_name = col_name.to_string()
                        data_normalyzed_str = idx
                        data_normalyzed_items.append(data_normalyzed_str)
                        data_normalyzed_str = f"{col_name}_items".replace(
                            f"    {self.champion}", "")
                        data_normalyzed_items.append(data_normalyzed_str)
        try:
            counter = 0
            dif_itm = []
            for i in range(int((len(data_normalyzed_items)-1)/2)+1):
                row_ = int(data_normalyzed_items[counter])
                col_ = data_normalyzed_items[counter + 1]
                counter += 2
                dif_itm.append(self.df_for_winners[col_].iloc[row_])
            # print(dif_itm)
        except:
            print("No data matched for champion items within your collection")

        analy_itm_names = []
        f = open("league_advisor/string_assets/items.json")
        data = json.load(f)
        data = data["data"]
        for item in dif_itm:
            for i in item:
                if i != 0:
                    analy_itm_names.append(data[f"{i}"]["name"])
        if analy_itm_names != []:
            return f"Our recommended build considering the composition: ==> {analy_itm_names}"
        else:
            print("Please try with another collections")


user_input = [["Nami", "Ezreal", "Syndra", "Nidalee", "Yone"], [
    "Blitzcranck", "Lillia", "Jax", "Sejuan", "Morgana"], "Ezreal"]
a = MatchData()
print(a.data_analyzer(user_input))   
print(a.data_analyzer_items())
