"""This module contains logos ascii art assets"""

from league_advisor.string_assets.colors import color

strings = {

    "logo_ascii": """

                                                                                                    
                                                                                                    
                  `sy+       `ssssssy.       +ss-         `:oyhddhy:   `ss+     `ss+  `ssssssy`            
                    hM+        hMo...:`      .NyNN.      `sNh/.   `:-    hM+      hM+   hMo...:`            
                    hM+        yM+          `dh /Md     .NM/             hM+      hM/   hM+                 
                    hM+        yMmddm       ym`  sMy    sMm        -::   hM+      hM/   hMmddd              
                    hM+        yM+         oMyyyyydMo   oMN`       :MN   hM+      hM/   hM+                 
                    hM+     `  yM+        /M/     `mM:   hMm:      -MN   yMy      mM/   hM+                 
                    dMdsssydo  dMdsssyhy :Nh       -MN:   :yNmyo+++yMN   `hMdo++sdmMo   mMdsssyhs           
                  `--------  `--------``---       `---`     .:////:-`     `://:. .--  `--------`           
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                  dmm:      `hmdhhhdhs:   -mm:      +my `dmo   +hmdhdmh     -sddhhdmds-    /mmhyddy-       
                  +N/NN.      sMo    .oMm:  /Mm`     yN.  dM/  oMm`    .   .dMo`     :dMh`  .MM   -MM:      
                -M/ :Mm`     sMo      :MM-  sMh    +M:   dM/  :NMy/`     `NM/         hMd  .MM   /Mm.      
                .Nd:::hMh     sMo       NM+   dM+  -Mo    dM/   `/sdMmy/  :MM`         :MM` .MM.hNy:        
              `dd/////hMs    sMo      -MN.   .NM-`Ny     dM/       `:dMm `NMo         sMd  .MM -mN+        
              yN.     `mM/   sMo    .oNm-     /Mmdm`     dM/  :`     +Mm  -mMs.     .sMh`  .MM  `sMd-      
            `sNs       /NN/ `hNmddddds:        +NN.     `mNs  +Nmdhdmd+`    /ymdhyhdds-    /NN-   .yNh:    
                                          `               ```            ```                        
                                                                                                    
                                                                                                    

    """,

    "welcome_message": """
     Welcome summoner! Get ready to start playing League of Legends like a pro! League Advisor will provide you with all you need to know to get started with the game.
     """,



    "main_menu": """

    For new users, enter (h)elp to show all available features and how to operate this program, then (d)iscover the game and learn the rules.

    For experienced summoners, (b)rowse the champions and items, get your (s)olo lane build, or raise the stakes and get your (r)anked queue build ready in an instant!"""
    """

    To stop the program, enter (q)uit.""",

  "main_menu_color" : f"""

    For new users, enter ({color.RED}h{color.RESET})elp to show all available features and how to operate this program, then ({color.RED}d{color.RESET})iscover the game and learn the rules.

    For experienced summoners, ({color.RED}b{color.RESET})rowse the champions and items, get your ({color.RED}s{color.RESET})olo lane build, or raise the stakes and get your ({color.RED}r{color.RESET})anked queue build ready in an instant!
 
    To stop the program, enter ({color.RED}q{color.RESET})uit.""",

    "help_list": """
        (h): help, provides a list of available features and commands, this is how you got here.

        (d): discover, provides printed text of game description and rules.

        (b): browse, provides a list of items or champions to choose from, and select a specific one to view its' stats.

        (s): solo, provides the optimal build path for one champion.

        (r): ranked, provieds the statically superior build based on its' win rate based on your team and the enemy's.

        (q): quit, quits the program.
    """,
    "item_list": ['Abyssal Mask', 'Aegis of the Legion', 'Aether Wisp', 'Amplifying Tome', "Anathema's Chains", "Archangel's Staff", 'Ardent Censer', 'B. F. Sword', "Bami's Cinder", 'Bandleglass Mirror', "Banshee's Veil", "Berserker's Greaves", 'Black Cleaver', 'Black Mist Scythe', 'Blade of The Ruined King', 'Blasting Wand', 'Blighting Jewel', 'Bloodthirster', 'Boots', 'Boots of Swiftness', 'Bramble Vest', 'Broken Stopwatch', 'Broken Stopwatch', 'Bulwark of the Mountain', "Caulfield's Warhammer", 'Chain Vest', 'Chempunk Chainsword', 'Chemtech Putrifier', 'Cloak of Agility', 'Cloth Armor', 'Commencing Stopwatch', 'Control Ward', 'Corrupting Potion', 'Cosmic Drive', 'Crystalline Bracer', 'Cull', 'Dagger', 'Dark Seal', "Dead Man's Plate", "Death's Dance", 'Demonic Embrace', 'Divine Sunderer', "Doran's Blade", "Doran's Ring", "Doran's Shield", 'Duskblade of Draktharr', 'Eclipse', 'Edge of Night', 'Elixir of Iron', 'Elixir of Sorcery', 'Elixir of Wrath', 'Emberknife', 'Essence Reaver', 'Everfrost', "Executioner's Calling", 'Eye of the Herald', 'Faerie Charm', 'Farsight Alteration', 'Fiendish Codex', 'Forbidden Idol', 'Force of Nature', 'Frostfang', 'Frostfire Gauntlet', 'Frozen Heart', 'Galeforce', 'Gargoyle Stoneplate', "Giant's Belt", 'Glacial Buckler', 'Goredrinker', 'Guardian Angel', "Guardian's Blade", "Guardian's Hammer", "Guardian's Horn", "Guardian's Orb", "Guinsoo's Rageblade", 'Hailblade', 'Harrowing Crescent', 'Health Potion', 'Hearthbound Axe', 'Hexdrinker', 'Hextech Alternator', 'Hextech Rocketbelt', 'Horizon Focus', 'Hullbreaker', 'Immortal Shieldbow', 'Imperial Mandate', 'Infinity Edge', 'Ionian Boots of Lucidity', 'Ironspike Whip', "Kalista's Black Spear", 'Kindlegem', 'Kircheis Shard', "Knight's Vow", 'Kraken Slayer', 'Last Whisper', 'Leeching Leer', "Liandry's Anguish", 'Lich Bane', 'Locket of the Iron Solari', 'Long Sword', "Lord Dominik's Regards", 'Lost Chapter', "Luden's Tempest", 'Manamune', 'Maw of Malmortius', "Mejai's Soulstealer", 'Mercurial Scimitar', "Mercury's Treads", "Mikael's Blessing", 'Minion Dematerializer', 'Mobility Boots', 'Moonstone Renewer', 'Morellonomicon', 'Mortal Reminder', 'Muramana', "Nashor's Tooth", 'Navori Quickblades', 'Needlessly Large Rod', 'Negatron Cloak', 'Night Harvester', 'Noonquiver', 'Null-Magic Mantle', 'Oblivion Orb', 'Oracle Lens', 'Pauldrons of Whiterock', 'Perfectly Timed Stopwatch', 'Phage', 'Phantom Dancer', 'Pickaxe', 'Plated Steelcaps', 'Poro-Snax', "Prowler's Claw", 'Quicksilver Sash', "Rabadon's Deathcap", 'Rageknife', "Randuin's Omen", 'Rapid Firecannon', 'Ravenous Hydra', 'Recurve Bow', 'Redemption', 'Refillable Potion', 'Rejuvenation Bead', 'Relic Shield', 'Riftmaker', 'Ruby Crystal', "Runaan's Hurricane", 'Runesteel Spaulders', "Rylai's Crystal Scepter", 'Sapphire Crystal', 'Scarecrow Effigy', "Seeker's Armguard", "Seraph's Embrace", "Serpent's Fang", 'Serrated Dirk', "Serylda's Grudge", 'Shard of True Ice', 'Sheen', "Shurelya's Battlesong", 'Silvermere Dawn', 'Slightly Magical Footwear', "Sorcerer's Shoes", 'Spectral Sickle', "Spectre's Cowl", "Spellthief's Edge", 'Spirit Visage', 'Staff of Flowing Water', 'Stealth Ward', 'Steel Shoulderguards', "Sterak's Gage", 'Stopwatch', 'Stormrazor', 'Stridebreaker', 'Sunfire Aegis', "Targon's Buckler", 'Tear of the Goddess', 'The Collector', 'The Golden Spatula', 'Thornmail', 'Tiamat', 'Titanic Hydra', 'Total Biscuit of Everlasting Will', 'Trinity Force', 'Turbo Chemtank', 'Umbral Glaive', 'Vampiric Scepter', 'Verdant Barrier', 'Vigilant Wardstone', 'Void Staff', "Warden's Mail", "Warmog's Armor", 'Watchful Wardstone', 'Winged Moonplate', "Wit's End", "Youmuu's Ghostblade", 'Your Cut', 'Zeal', "Zeke's Convergence", "Zhonya's Hourglass"],


    "champion_list_upper": ['Aatrox', 'Ahri', 'Akali', 'Akshan', 'Alistar', 'Amumu', 'Anivia', 'Annie', 'Aphelios', 'Ashe', 'Aurelion Sol', 'Azir', 'Bard', 'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Camille', 'Cassiopeia', "Cho'Gath", 'Corki', 'Darius', 'Diana', 'Draven', 'Dr. Mundo', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Heimerdinger', 'Illaoi', 'Irelia', 'Ivern', 'Janna', 'Jarvan IV', 'Jax', 'Jayce', 'Jhin', 'Jinx', "Kai'Sa", 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kayn', 'Kennen', "Kha'Zix", 'Kindred', 'Kled', "Kog'Maw", 'LeBlanc', 'Lee Sin', 'Leona', 'Lillia', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar', 'Maokai', 'Master Yi', 'Miss Fortune', 'Wukong', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus', 'Nautilus', 'Neeko', 'Nidalee', 'Nocturne', 'Nunu & Willump', 'Olaf', 'Orianna', 'Ornn', 'Pantheon', 'Poppy', 'Pyke', 'Qiyana', 'Quinn', 'Rakan', 'Rammus', "Rek'Sai", 'Rell', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Samira', 'Sejuani', 'Senna', 'Seraphine', 'Sett', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona', 'Soraka', 'Swain', 'Sylas', 'Syndra', 'Tahm Kench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'Twisted Fate', 'Twitch', 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar', "Vel'Koz", 'Vex', 'Vi', 'Viego', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Xayah', 'Xerath', 'Xin Zhao', 'Yasuo', 'Yone', 'Yorick', 'Yuumi', 'Zac', 'Zed', 'Ziggs', 'Zilean', 'Zoe', 'Zyra'],


    "champion_list_lower": ['aatrox', 'ahri', 'akali', 'akshan', 'alistar', 'amumu', 'anivia', 'annie', 'aphelios', 'ashe', 'aurelion sol', 'azir', 'bard', 'blitzcrank', 'brand', 'braum', 'caitlyn', 'camille', 'cassiopeia', "cho'gath", 'corki', 'darius', 'diana', 'draven', 'dr. mundo', 'ekko', 'elise', 'evelynn', 'ezreal', 'fiddlesticks', 'fiora', 'fizz', 'galio', 'gangplank', 'garen', 'gnar', 'gragas', 'graves', 'gwen', 'hecarim', 'heimerdinger', 'illaoi', 'irelia', 'ivern', 'janna', 'jarvan iv', 'jax', 'jayce', 'jhin', 'jinx', "kai'sa", 'kalista', 'karma', 'karthus', 'kassadin', 'katarina', 'kayle', 'kayn', 'kennen', "kha'zix", 'kindred', 'kled', "kog'maw", 'leblanc', 'lee sin', 'leona', 'lillia', 'lissandra', 'lucian', 'lulu', 'lux', 'malphite', 'malzahar', 'maokai', 'master yi', 'miss fortune', 'wukong', 'mordekaiser', 'morgana', 'nami', 'nasus', 'nautilus', 'neeko', 'nidalee', 'nocturne', 'nunu & willump', 'olaf', 'orianna', 'ornn', 'pantheon', 'poppy', 'pyke', 'qiyana', 'quinn', 'rakan', 'rammus', "rek'sai", 'rell', 'renekton', 'rengar', 'riven', 'rumble', 'ryze', 'samira', 'sejuani', 'senna', 'seraphine', 'sett', 'shaco', 'shen', 'shyvana', 'singed', 'sion', 'sivir', 'skarner', 'sona', 'soraka', 'swain', 'sylas', 'syndra', 'tahm kench', 'taliyah', 'talon', 'taric', 'teemo', 'thresh', 'tristana', 'trundle', 'tryndamere', 'twisted fate', 'twitch', 'udyr', 'urgot', 'varus', 'vayne', 'veigar', "vel'koz", 'vex', 'vi', 'viego', 'viktor', 'vladimir', 'volibear', 'warwick', 'xayah', 'xerath', 'xin zhao', 'yasuo', 'yone', 'yorick', 'yuumi', 'zac', 'zed', 'ziggs', 'zilean', 'zoe', 'zyra'],


      "help_list_color" : f"""
        ({color.RED}h{color.RESET}): help, provides a list of available features and commands, this is how you got here.

        ({color.RED}d{color.RESET}): discover, provides printed text of game description and rules.

        ({color.RED}b{color.RESET}): browse, provides a list of items or champions to choose from, and select a specific one to view its' stats.

        ({color.RED}s{color.RESET}): solo, provides the optimal build path for one champion.

        ({color.RED}r{color.RESET}): ranked, provieds the statically superior build based on its' win rate based on your team and the enemy's.

        ({color.RED}q{color.RESET}): quit, quits the program.
    """,

    "disc" : f"""
        
        
        League of Legends is one of the world's most popular video games, developed by Riot Games. 

        It features a team-based competitive game mode based on strategy and outplaying opponents.

        League of Legends is a MOBA (Multiplayer Online Battle Arena) type of game.

        Two teams 5 players battle each other on a chosen map. 

        The game's objective is to destroy the key building in enemy base - the Nexus. 

        The gameplay combines use of skill and tactics, and there are many roads to victory. 

        There are plenty of things that a player needs to keep an eye on, such as map visibility,
         enemies spotted on the lane, as well as those who may suddenly appear on the frontline.

        Outnumbering your opponent may often turn out to be the key to success.

        LoL offers three game modes: Classic (maps: Summoner's Rift), and ARAM (Howling Abyss),
         which are detailed further in the guide.

        League of Legends is based on microtransactions. Downloading and playing the game is free.
 
        All in-game champions, runes, and runebook pages can be purchased with BE (Blue Essence),
        which are awarded to each player for their sheer participation in battles.

        Real money can be spent on OE (Orange Essence), which allow players to buy additional skins for their champions. 

        Skins are just a visual aspect - they do not influence champions' statistics. 

        Another benefit of having OE is that you can spend them to immediately purchase champions of your interest. 

        Only runes are available exclusively for BE. Owing to its attractiveness and mechanics LoL has quickly
        become the most popular e-sport in the world. 

        To discover more about League of Legends, visit the official website at https://www.leagueoflegends.com.

        To go back to main menu , press any key.
       """,

       "disc_color" : f"""
        
        
        League of Legends is one of the world's most popular video games, developed by Riot Games. 

        It features a team-based competitive game mode based on strategy and outplaying opponents.

        League of Legends is a MOBA (Multiplayer Online Battle Arena) type of game.

        Two teams 5 players battle each other on a chosen map. 

        The game's objective is to destroy the key building in enemy base - the Nexus. 

        The gameplay combines use of skill and tactics, and there are many roads to victory. 

        There are plenty of things that a player needs to keep an eye on, such as map visibility,
         enemies spotted on the lane, as well as those who may suddenly appear on the frontline.

        Outnumbering your opponent may often turn out to be the key to success.

        LoL offers three game modes: Classic (maps: Summoner's Rift), and ARAM (Howling Abyss),
        which are detailed further in the guide.

        League of Legends is based on microtransactions. Downloading and playing the game is free.
 
        All in-game champions, runes, and runebook pages can be purchased with BE (Blue Essence),
        which are awarded to each player for their sheer participation in battles.

        Real money can be spent on OE (Orange Essence), which allow players to buy additional skins for their champions. 

        Skins are just a visual aspect - they do not influence champions' statistics. 

        Another benefit of having OE is that you can spend them to immediately purchase champions of your interest. 

        Only runes are available exclusively for BE. Owing to its attractiveness and mechanics LoL has quickly
        become the most popular e-sport in the world. 

        To discover more about League of Legends, visit the official website at {color.BLUE}https://www.leagueoflegends.com{color.RESET}.

        {color.RED}To go back to main menu , press any key.{color.RESET}
       """
}
