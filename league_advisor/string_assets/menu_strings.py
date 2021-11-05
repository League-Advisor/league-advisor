"""This module contains logos ascii art assets"""

from string_assets.colors import color

strings = {

  "logo_ascii" : """
                `...-:-        `-:::::::---:-      .:....:-          `..--------.`    `...-:      `----: .-.-----::://                                 
                  .:-:/+        .://///////:/+       ::----+.      ``...---::::-----.  `..--o      .-..-o .---:://+++os`                                
                  `-://o        .:://sooooo++-      `---:---+`    `....-+oo+++oo+:::+: `..--o      ...--o .---+o+++++++   `````    `````                
                  `:://o        .:://s`            `----so..-/   `-.../s/.     `:+oo+. `...-o      .-.--s -:-:o-        `-/+o+/-``-:///+`               
                  `:/++o        `::/:/----.--      .---+//:../:  -...:s.    `````.-.````....o      .----s -:-://:::/// `/+ssooo++.:/so++`               
                  `:/++o        `::/:::::::+:     .---+o` /-../. -...+/    ------..---/`...`+      .----s -:::://++oss`-oo+`  -+++/++++.                
                  `:/++o        `::/:sooooo+`    `--.-+-``.-...+`:--.:o   .+ooooo/...-o.....o      .---:o -:::+sooooo- `oo+--:/oo++oso+.                
                  `::++o        `/:::o          `-.......-....../`+/--/:`  .----:-..:+:`--..s.     .---:o -:::o-        `+sosyys/`/so                   
                  `-/+++-.......`/://+-......` `....+oooooooo-..-:.+/:----......-.-:+o` :/-.-:-...-----s: -:::o:-------   `-::-`  `-.                   
                  `:++++++////o/`/:///:::---:/ ..../o........+...:-`/o+/::-..----:+s/`   :+::--------+s+  -/:////++ooos                                 
                `-ossssssssoos.`/ossssoooo+o/`/+++s`        `:/++o` `:ossysooosso/`      ./osooooooso-   -osssssssssss`                                
                  `...........`  `...........` `...`           ....      `--::-.`            `--::-.       ...........`                                 
                `...--`        `..----------`     ```.......``     ```.....-..--`...--:        `....```....--:--.`         `.---::-.` `                
                  -::/++        `::////:::--:/   `...........---.   -.......---:s`::::-:+`      .-..::`.--://++/++++:`    .:/++++o+++o/`                
                  ./:+o+        .//+/osssssoo/ `.--.-/ossooo/...:/  --../ooooooos`./--..-+-     ....:/`::::+osssoo++oo/  .+osossssysooy+                
                  ./:/++        .//+/s.`````` .----+y+-````./o/+so` --..+-``````` .:..--..//`   .-.-//`::::o...-:oyooos+ /+ooy+````:os+-                
                  ./:/++        .//+/s-.....``::--so`        `::.`  --../-``````  .:.-/y:--:+.  .:--//`:://o      .yosss-/++oo+:-...``                  
                  ./-//+        ./+++++/::-+/.::--h`   `...--.----/`--....-.---o` .:--////-.-+: .:--//`/://o       -sooo+`+o++++/////:-                 
                  `/-:/+        .++o+osssooy.`/:::y`   ://++++:-::o.-:--/o+o++o/  .::-+: -+---:+::-://`//++o       -ooooo `-ossoooo///++                
                  `/-:/+        `++oos-.....  /+/:++`  -+++++o:::/s`::--o:.....`  .:--+:  .+:--:+:::+/`//+oo      ./o++s/ `.:`.-:/+o///+:               
                  `:-:/o``````` `+/oos.`````` `/++++/-.````.-:::/s/ ::::o-``````` .:--/:   `:+/:::::+/`++oos....-/++++so.-/:+/.````:::/o+               
                  .-::///://+//:`//+ooo++++++: `/oo+++//::/:::/os/  -:////::::::/ .:-:/:     .++///++/`//ossso++++++os+` :o+/////////:+s-               
                  -/+++++++ooos-`:+oooosooooo/   ./oossooooo+os+.   -/++++++++++o``////-      `/++ooo/`++ssssoooosso/.    -+ssooo++++so-                
                  .///////////:  -///////////.     `-:++oo++/-`     `///////////:  :///`        .////. -/////////-.`        .:/+oo++:.  
  


      Welcome summoner! Get ready to start playing League of Legends like a pro! League Advisor will provide you with all you need to know to get started with the game.
  """,

  "main_menu" : """

    For new users, enter (""" + color.RED + "h" + color.RESET + """)elp to show all available features and how to operate this program, then (""" + color.RED + "d" + color.RESET + """)iscover the game and learn the rules.

    For experienced summoners, (""" + color.RED + "b" + color.RESET + """)rowse the champions and items, get your (""" + color.RED + "s" + color.RESET + """)olo lane build, or raise the stakes and get your (""" + color.RED + "r" + color.RESET + """)anked queue build ready in an instant!""" + "\n"
    """
    To stop the program, enter (""" + color.RED + "q" + color.RESET +""")uit.""",


  "help_list" : """
        (h): help, provides a list of available features and commands, this is how you got here.

        (d): discover, provides printed text of game description and rules.

        (b): browse, provides a list of items or champions to choose from, and select a specific one to view its' stats.

        (s): solo, provides the optimal build path for one champion.

        (r): ranked, provieds the statically superior build based on its' win rate based on your team and the enemy's.

        (q): quit, quits the program.
    """,
}