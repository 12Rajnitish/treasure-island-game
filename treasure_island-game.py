print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

def to_the_cave():
    print("The cave is dark and damp. The treasure chest lies in the center, surrounded by glowing candles.")
    print(r'''
            ,,'6''-,.
            <====,.;;--.
            _`---===. """==__
          //""@@-\===\@@@@ ""\\
         |( @@@  |===|  @@@  ||
          \\ @@   |===|  @@  //
            \\ @@ |===|@@@ //
             \\  |===|  //
    ___________\\|===| //_____,----""""""""""-----,_ 
      """"---,__`\===`/ _________,---------,____    `, 
                 |==||                           `\   \ 
                |==| |          pb                 )   | 
               |==| |       _____         ______,--'   ' 
               |=|  `----"""     `""""""""         _,-' 
                `=\     __,---"""-------------"""'' 
                    """'
    ''')

    print("Suddenly, a giant cobra emerges, its eyes locking onto yours."
          "\nTo take the treasure, answer my riddle:")

    print("I speak without a mouth and hear without ears.\n"
          "I have no body, but I come alive with the wind. What am I?\n"
          "What is your answer?\n")

    choice=input("1.Shadow\n"
                 "2.Echo\n"
                 "3.Whisper\n"
                 "Press 1, 2 or 3\n")
    if choice=='1' or choice=='3':
        print("The cobra strikes quickly, its fangs sinking deep into your neck. Darkness overtakes you.\n"
              "Game Over.\n"
              "The island claims another victim.")
    elif choice=='2':
        print("The cobra hisses and moves aside, revealing the treasure chest.\nYou’ve won—for now.\n")
        print("Congratulations! You've found the treasure, but the island's curse never leaves.\n"
              "Something watches from the shadows...")
    else:
        print("Wrong choice.\nThe cobra recoils and strikes. Venom floods your body, and you collapse to the ground.\n"
              "Game Over.\n"
              "The island claims another victim.")

#The discovery of the Island
print("You’re sitting on a foggy beach when you find an old bottle buried in the sand.")
print("Inside is a map to a hidden treasure, along with a note:")
print("The treasure is real, but beware—the island has claimed many before you.")
print("Will you follow the map or walk away?")

choice1=input("1.Go for the treasure.\n2.Leave the map\n")
if choice1=='1':
    print("You decide to go after the treasure. Careful, There's no turning back now.")
    print("You finally reach the island, the air thick with the smell of decay.\n"
          "The map shows three paths, but each feels wrong.\n"
          "Which way will you go?\n")

    choice2=input("Through the jungle.\n"
               "Over the hill to the killer tribe.\n"
               "Along the beach\n"
               "Type Jungle, Hill or Beach\n").lower()

    if choice2=='jungle':
        print("The jungle is alive with sounds. Suddenly, a wild boar charges at you with glowing eyes.\n"
              "What will you do?")

        print(r'''
        ***********************************************
                      _,-""""-..__
                 |`,-'_. `  ` ``  `--'""".
                 ;  ,'  | ``  ` `  ` ```  `.
               ,-'   ..-' ` ` `` `  `` `  ` |==.
             ,'    #    `  `    `` `  ` `.  ;   \
            `}_,-^-   _ .  ` \ `  ` __ `   ;    #
               `"---"' `-`. ` \---""`.`.  `;
                          \\` ;       ; `. `,
                           ||`;      / / | |
            grunts         //_;`    ,_;' ,_;"
        ***********************************************
        ''')

        choice3=input("Fight the Boar.\n"
                      "Run away\nType Fight or Run\n").lower()
        if choice3=='fight':
            print("You manage to kill the boar, but its blood stains your hands.\n"
                  "A strange laugh echoes from the trees.\n")
            to_the_cave()

        elif choice3=='run':
            print("You turn and flee, but fall into a hidden pit. Pirates' voices grow closer.\n")
            print("Game Over.\n"
                  "The island claims another victim.")
        else:
            print("Wrong choice. Game Over\n"
                  "The island claims another victim.")


    elif choice2=='hill':
        print("As you reach the top of the hill, strange figures emerge. Their eyes glow in the dark.\n"
              "What will you do?")

        print(r'''
                ********************************
                                     ==\\
                             || \\
                          ________\
                         |________|\ 
                         | *\  /* | \
                        {|   ^^   |}
                          \ /||\ /
                           \|__|/
                      =____||  ||____=
               \\/\    /                \    /\//
              \\/  \  /           .      \  /  \//
               /    \/                    \/    \
                \            .                 /
                 \                            /
                  \_                        _/
                              .
            .                                   .
                             .  .

                    (         .       )
                 ( (   (                ) .
              .   (       .          .     )   )
                (    (        .   .          )
         .  ( (   .     (              )  )        )
             ( .            .
           (        .              .
        ..       .       .                    .

                                                  .
            .           .                 .
        You shouldn't be here!

        *************************************************
        ''')

        choice4=input("Try to negotiate.\n"
                      "Run back down as fast as you can.\n"
                      "Press N or R\n").lower()
        if choice4=='n':
            print("One of the tribe shoots you with an arrow. You fall lifeless to the ground.\n"
                  "Game Over.\n"
                  "The island claims another victim.")
        else:
            print("You fall into a pit filled with sharp rocks. Your last breath escapes as you die.\n"
                  "Game Over.\n"
                  "The island claims another victim.")


    elif choice2=='beach':
        print(r'''
                         _____
                      .-" .-. "-.
                    _/ '=(0.0)=' \_
                  /`   .='|m|'=.   `\
                  \________________ /
              .--.__///`'-,__~\\\\~`
             / /6|__\// a (__)-\\\\
             \ \/--`((   ._\   ,)))
             /  \\  ))\  -==-  (O)( 
            /    )\((((\   .  /)))) 
           /  _.' /  __(`~~~~`)__ 
          //"\\,-'-"`   `~~~~\\~~`"-.
         //  /`"              `      `\
        //
        ''')
        print("You spot a pirate camp. The fire casts long shadows, and their laughter chills you to the bone.\n"
              "What will you do?\n")

        choice5=input("Fight the pirates.\n"
                      "Sneak past them.\n"
                      "Type Fight or Sneak\n").lower()
        if choice5=='fight':
            print("You charge at them, but they open a trapdoor beneath you. You fall into the darkness.\n"
                  "Game Over.\n"
                  "The island claims another victim.")
        else:
            print("You manage to sneak by, but the sound of the fire grows distant as you near a cave.")
            to_the_cave()
    else:
        print("Wrong choice.\n"
              "Game Over.\n"
              "The island claims another victim.")

elif choice1=='2':
    print("You toss the map back into the sea, walking away from the cursed shore.")
    print("Game Over.\n"
          "The island claims another victim.")

else:
    print("You give me the wrong answer\nGame Over.\n"
          "The island claims another victim.")

