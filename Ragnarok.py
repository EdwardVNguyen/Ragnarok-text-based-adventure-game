import time


# References - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# “Writing a Text-Based Adventure Game in Python.” YouTube, YouTube, 26 Apr. 2016,
# https://www.youtube.com/watch?v=miuHrP2O7Jw&amp;t=836s.
# user2745401user2745401 78711 gold badge55 silver badges33 bronze badges, et al. “How to Check If a String Only
# Contains Letters?” Stack Overflow, 1 Nov. 1960,
# https://stackoverflow.com/questions/18667410/how-to-check-if-a-string-only-contains-letters.
# Joan VengeJoan Venge 304k209209 gold badges467467 silver badges676676 bronze badges, et al.
# “How to Check If the String Is Empty?” Stack
# Overflow, 1 Apr. 1959, https://stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty.

class Character:
    def __init__(self, favour=0, physical_lvl=0, magic_lvl=0):
        self.favour = favour
        self.physical_lvl = physical_lvl
        self.magic_lvl = magic_lvl


# user's character
user_character = Character()
traits = 'temperance'  # Traits for user's character --> affects story
user_name = 'Power'  # Simply a filler name for testing purposes
weapon = 'fist'  # weapon for testing purpose
pet = 'none'

# NPC characters
npc_delphine = Character()
npc_victor = Character()
npc_lucy = Character()


# Useful functions

def loading(amount_of_dots):
    loading_dot = '.'
    for i in range(amount_of_dots):
        print(loading_dot)
        loading_dot += loading_dot
        time.sleep(1)


def read_dialogue(dialogue, time_between_dialogue):
    for line in dialogue:
        print(line)
        time.sleep(time_between_dialogue)


def completion_of_level(level_name):
    print('\n---------------------------------------------------------')
    print(str(level_name))
    print('---------------------------------------------------------\n')
    time.sleep(2)


def user_choice(option1, option2, option3, option4):
    print('--------------------------------------------')
    print(f'1. {option1}')
    print(f'2. {option2}')
    print(f'3. {option3}')
    print(f'4. {option4}')
    print('--------------------------------------------')

    choice = str(input('What action will you take?: '))

    while (choice != '1') and (choice != '2') and (choice != '3') and (choice != '4'):
        choice = str(input('What action will you take?: '))

    return choice


# ACT 1 - - - Chapter 1 - - - - - - - - - - - - - - - -

def start_game():
    start = ''
    while start != '1':
        start = str(input("Start game? Type \'1\' to start: "))
    loading(7)

    dialogue1 = ["\nA muffled voice. . . You hear something or someone calling out to you. . . .",
                 "You can barely understand what they are saying. . .",
                 "Your name?",
                 "I think it wants to know your name?"
                 ]
    read_dialogue(dialogue1, 3)

    #  User gets their names - - - - - - - - - - - - - - - - - - - - - - - - -
    global user_name
    user_name = str(input("My name is: "))

    def check_name(name):

        while (name == '') or (not name.isalpha()):
            if name == '':
                print("You must have a name! It can't be empty!")
                name = str(input("My name is: "))

            if not name.isalpha():
                print("You must only have letters!")
                name = str(input("My name is: "))

        confirmation = ''

        while (confirmation != '1') and (confirmation != '2'):
            confirmation = str(input('Are you sure this is your name? 1. Yes 2. No : '))

        if confirmation == '1':
            global user_name
            user_name = name

        if confirmation == '2':
            name = str(input("My name is: "))
            check_name(name)

    check_name(user_name)
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    loading(3)

    dialogue2 = ['\n' + user_name + '?',
                 '"Yes! ' + user_name + ' is my name!"',
                 'You roar to the top of your lungs. . .',
                 '"My name is ' + user_name + '!"'
                 ]
    read_dialogue(dialogue2, 2)
    loading(5)
    completion_of_level('Chapter 1: Beginnings')
    loading(7)


# Cave level - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def cave_level():
    time.sleep(2)

    dialogue1 = ['\nUnknown Man: Holy crap! The dead are talking now! We really are doomed!',
                 'Unknown Women: Oh shut up!',
                 'Unknown Women: Just keep on shooting those fireballs Victor!',
                 'Unknown Women: We need to keep pushing them back!',
                 'Unknown Women: Asmund and Alex! I need you two to hold the left tunnel!',
                 'Unknown Women: I\'ll hold the right!',
                 'Unknown Women: Lucy! Go check up on the refugees! Make sure they don\'t have any bite marks!'
                 ]
    read_dialogue(dialogue1, 2)
    loading(3)

    dialogue2 = ['\nLucy: ' + user_name + '?',
                 '"Who are you?"',
                 'Lucy: I\'m Lucy, you seem badly hurt. . .',
                 'Lucy: I\'m sorry but I\'m going to need to take off your shirt to check for any bite marks. . .',
                 '"Where am I?"',
                 'Lucy: We\'re in a cave right now, right outside of Pirewood village. . .',
                 '.',
                 '. .',
                 '. . .',
                 '"Who am I?"\n'
                 ]
    read_dialogue(dialogue2, 4)
    time.sleep(2)

    dialogue3 = ['Lucy: Do you really not know who you are? It seems like you know your name though. . .',
                 '* Lucy finishes checking up on you and gives you back your shirt *',
                 'Lucy: Well. . I need to get going, I need to check up on the other refugees',
                 'Lucy: I\'ll talk with you later, kay?'
                 ]
    read_dialogue(dialogue3, 3)
    loading(4)

    dialogue4 = ['* From the corner of your eyes, you see an animated corpse right behind Lucy *',
                 '* It looks like its about the bite her! * ',
                 '* You see a stick right next to you! *'
                 ]
    read_dialogue(dialogue4, 3)

    choice = user_choice('Grab the stick and try to cast a spell',
                         'Grab the stick and attack the zombie with it',
                         'Punch the zombie with your fist instead',
                         'Yell out to Lucy'
                         )

    if choice == '1':
        global weapon
        weapon = 'stick'
        user_character.magic_lvl += 1

        dialogue = ['* You picked up the stick *',
                    '* A small orb of fire emits, you fire at the zombie *',
                    '* You turned the zombie\'s attention away from Lucy, however its now coming towards you! *',
                    '* You try to muster another spell however you are too fatigued from the last cast *'
                    ]
        read_dialogue(dialogue, 2)

        choice = user_choice('Call for help',
                             'Keep on trying to cast a spell',
                             'Try to run away',
                             'Yell out to Lucy'
                             )
        introduction_victor(choice)

    elif choice == '2':
        dialogue = ['* You poke the zombie with the stick... *',
                    '* You are unsure, but is that zombie. . . *',
                    '* Disappointed in you??? *',
                    '* . . . . *',
                    '* . . . *',
                    '* . .  *',
                    '* .  *',
                    '* After the stare down, the zombie seems like it has enough with your antics *',
                    '* You think to yourself that it probably is a good idea to call on Lucy *',
                    ]
        read_dialogue(dialogue, 3)
        introduction_lucy()

    elif choice == '3':
        weapon = 'fist'

        dialogue = ['* You punch the zombie by the skull!',
                    '* A critical hit! *',
                    '* The zombie seems dazed *',
                    '"What should I do now?"'
                    ]
        read_dialogue(dialogue, 3)

        choice = user_choice('Give up?',
                             'Call for Lucy',
                             'Punch the zombie again',
                             'Pick up the stick and jab the zombie in the eyeballs!'
                             )
        after_punch_scene_scenario(choice)

    elif choice == '4':
        introduction_lucy()


def introduction_victor(choice):
    victor_dialogue = ['* It seems hopeless, the zombie marches towards you *',
                       '* Then all of a sudden, a massive fireball flies past you, obliterating the zombie *',
                       '"Holy!"',
                       'Unknown Man: I was not expecting another mage!',
                       'Unknown Man: I won\'t lie though, that fireball of yours was fairly weak! Haha!',
                       'Victor: I heard your cry for help! Name\'s Victor!',
                       'Victor: Shoot! I\'ll talk with you later, I have a horde to keep at bay!'
                       ]

    if choice == '1':
        dialogue = ['* You call for help *',
                    '"Help! Somebody help me!"',
                    '* You can\'t run, your legs are too weak to even move *',
                    ]
        read_dialogue(dialogue, 2)
        read_dialogue(victor_dialogue, 2)
        npc_victor.favour += 1

    elif choice == '2':
        dialogue = ['* You try to cast a spell *',
                    '* Its no use! You don\'t have any mana left! *'
                    ]
        read_dialogue(dialogue, 2)
        read_dialogue(victor_dialogue, 2)
        npc_victor.favour += 1

    elif choice == '3':
        dialogue = ['* You try to run away! *',
                    '* However, you can\'t run! Your legs are too weak to even move *',
                    ]
        read_dialogue(dialogue, 2)
        read_dialogue(victor_dialogue, 2)
        npc_victor.favour += 1

    elif choice == '4':
        introduction_lucy()


def introduction_lucy():
    global pet
    pet = 'Kon'

    dialogue = ['* You call out to Lucy *',
                '* In the nick of time, Lucy faces towards the zombie and makes some sort of hand signal *',
                '* Mist comes from beneath the ground *',
                '* Suddenly a fox the size of a panther appears! *',
                '* It swiftly makes quick work of the zombie *',
                '* You are unsure if it is an enemy or an ally *',
                'Lucy: Don\'t worry! This is one of my summons!',
                'Lucy: Thanks for calling out to me!',
                'Unknown Women: Lucy! Are you done checking the refugees?! I need you up here with me now!',
                'Lucy: Yes Delphine!',
                '* Before Lucy goes, she does another hand signal, summoning now a fox the size of a husky',
                'Lucy: Kon! Protect ' + user_name + '!',
                '* She runs off to support Delphine. . . *'
                ]
    read_dialogue(dialogue, 3)
    npc_lucy.favour += 1


def after_punch_scene_scenario(choice):
    if choice == '1':
        victor_dialogue = ['* It seems hopeless, the zombie marches towards you *',
                           '* Then all of a sudden, a massive fireball flies past you, obliterating the zombie *',
                           '"Holy!"',
                           'Victor: I saw you were in trouble! Name\'s Victor!',
                           'Victor: Shoot! Got to go! I have a horde to keep at bay!'
                           ]
        read_dialogue(victor_dialogue, 3)

    elif choice == '2':
        introduction_lucy()

    elif choice == '3':
        user_character.physical_lvl += 1
        dialogue = ['"Of course! The punch did daze the zombie, I just have to do it again!"',
                    '* You punch the zombie, it finally falling to the ground *',
                    '"I think it\'s dead now. . . phew . . "'
                    ]
        read_dialogue(dialogue, 3)

    elif choice == '4':
        user_character.physical_lvl += 1
        dialogue = ['* You pick up the stick and jab it inside the zombie\'s eyeballs. . *',
                    '* Wait! It\'s a zombie, it doesn\'t affect it at all! *',
                    '* You punch the zombie, it finally falls to the ground *',
                    '* I think it\'s dead now. . . phew . ."'
                    ]
        read_dialogue(dialogue, 3)


# Chapter 2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - -  - - -
def the_state_of_the_world():
    time.sleep(4)
    completion_of_level('Chapter 2: The State of The World')
    loading(4)

    dialogue1 = ['* The fight has been on going for quite a while *',
                 '* As your adrenaline wears down, you question the situation *',
                 '"Zombies? Am I in some sort of apocalypse?"',
                 '* The other refugees look at you strange *',
                 '* You wonder what you should do now *'
                 ]
    read_dialogue(dialogue1, 3)

    choice = user_choice('Wait it out',
                         'Ask one of the refugees what is happening',
                         'Check on the fighting',
                         'Examine the dead zombie'
                         )
    if choice == '1':
        print("* You decide to wait it off *")
        loading(4)

        dialogue = ['* You can still hear fighting off in the distance *',
                    '* You start to become bored after a while. . . *',
                    '* You hear a little girl blurt out why this is all happening *',
                    '* A middle man decides to speak, you decide to eavesdrop *'
                    ]
        read_dialogue(dialogue, 3)
        background_of_the_world()

    if choice == '2':
        dialogue = ['* You make your way across the cave *',
                    '* Refugees are starting to look at you *',
                    '* You place yourself in the middle of the crowd of refugees *',
                    '* After a couple minutes, you start off with saying . . . *',
                    '" Do any of you know what\'s going on?"',
                    '* About a third of the dozen refugees ignore you, two looking at you with surprise *',
                    '* A refugee the age of a middle old man decides to speaks with you *',
                    ]
        read_dialogue(dialogue, 3)
        background_of_the_world()

    if choice == '3':
        dialogue = ['* You decide to check on the fighting *',
                    '* You see a bloody battle between humans and zombies *',
                    '* It looks like a total of five humans are defending you and the refugees from what looks like '
                    'hundreds of zombies *',
                    '* You see that the human team is comprised of three warriors, one mage, and one summoner *',
                    '* You don\'t want to get in their way, so you decide to go back *',
                    '* Once you head back with the refugees, you hear them murmuring *',
                    '* You hear a little girl blurt out why this is all happening *',
                    '* A middle man decides to speak, you decide to eavesdrop *'
                    ]
        read_dialogue(dialogue, 3)
        background_of_the_world()

    if choice == '4':
        dialogue = ['* You decide to examine the dead zombie *',
                    '* Male, on the tallish side, skinny *',
                    '* You feel bad for it, after all it was once human *',
                    '* After a while, you hear the refugees murmuring *',
                    '* You hear a little girl blurt out why this is all happening * ',
                    '* A middle man decides to speak, you decide to eavesdrop *'
                    ]
        read_dialogue(dialogue, 3)
        background_of_the_world()


def background_of_the_world():
    loading(4)
    dialogue = ['\nRefugee: It all happened one year past, when the world fell into ruins',
                'Refugee: The queen of the Midgard killed her own husband, king Godfrey',
                'Refugee: God knows why. . However since king Godfrey\'s death, the World Tree has been faltering',
                'Refugee: As the tree grows weaker, the world will see more chaotic and evil forces awaken. . ',
                'Refugee: The undead are only the beginning. . .'
                ]
    read_dialogue(dialogue, 5)


# Chapter 3  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def to_solitude():
    time.sleep(4)
    completion_of_level('Chapter 3: Solitude')
    loading(4)

    dialogue1 = ['* After learning the background of the world, the refugee began to speak about the group of humans '
                 'protecting them *',
                 '* It seems like they call themselves the Blazing Stars, a group of adventurers *',
                 '* They are lead by Delphine, a swordswoman who comes from the countryside, you learn that she'
                 ' is a local celebrity in this region *',
                 '* Asmund and Alex, who are the other two warriors *',
                 '* Asmund comes from a line of great warriors, wielding a'
                 ' great axe, he is known for being righteous *',
                 '* Alex, someone who has been recently selected on the team, he is a novice swordsman but his heart is'
                 ' always in the right place *',
                 '* Victor, a mage who is known as a failed prodigy, deciding to go adventuring with the Blazing Stars '
                 'instead of pursing his studies at the College of Mages *',
                 '* And finally Lucy, the one who checked up on me, not much is known about her but it seems like she'
                 ' is a rare summoner type, she makes contracts with celestial spirits *'
                 ]
    read_dialogue(dialogue1, 5)
    loading(4)
    time.sleep(2)
    loading(4)
    time.sleep(2)

    dialogue2 = ['Delphine: ~huff~ ~ ~ huff~ ~ huff~ ~ ~. . .  .',
                 '* The fighting has ended, the group of adventurers return to the refugees *',
                 '* However there were only three of them *',
                 '* Delphine seems exhausted and her eyes are red, it seems like she was crying beforehand *',
                 'Delphine: Lucy. . .',
                 'Delphine: ~huff ~ ~ huff ~ . .',
                 'Delphine: Escort the refugees outside. . ~ huff ~',
                 'Delphine: Victor said. . .',
                 'Delphine: He found a wagon. . and some horses. . ~huff ~ huff ~ ~. . .',
                 '* Lucy looks like she is sweating as well. . *',
                 'Lucy: Yes Delphine. . . ',
                 '* The two warriors, Alex and Asmund did not make it *'
                 ]
    read_dialogue(dialogue2, 5)
    loading(4)

    dialogue3 = ['* We made it outside the cave *',
                 '* Outside, we were met with a vast landscape with dark clouds overlooking us *',
                 '* Birds chirped and hummed, it had seem that animal life still thrived in this region *',
                 '* The undead had only wanted human flesh *',
                 '* Because of this, the horses when we arrived had been in healthy shape *'
                 ]
    read_dialogue(dialogue3, 5)
    loading(4)

    dialogue4 = ['Refugee girl: Where are we going?',
                 'Delphine: We\'re headed to Solitude. .',
                 '"Solitude?"',
                 'Delphine: Yes, its a village up north, the undead have not reached that far so we should be safe '
                 'there.',
                 '* The refugees and I climbed the wagon *',
                 '* Delphine and Lucy decided to ride their horses lone *',
                 '* Victor attached the horses and we set off to Solitude *'
                 ]
    read_dialogue(dialogue4, 5)
    time.sleep(3)
    loading(7)


# Chapter 4 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def the_hermit():
    time.sleep(5)
    completion_of_level('Chapter 4: The Hermit')
    loading(4)

    dialogue1 = ['* From Pirewood village where we had first set off, we traversed through a great forest until'
                 ' we reached the plains *',
                 '* Unlike the gloominess of the forest, the sky was blue with clouds white *',
                 '* It was a peaceful ride throughout *',
                 '* In time we had reached Solitude, a humble village that secluded itself from the outside world *'
                 ]

    dialogue2 = ['Old Man: Hey! Whoever you are! Stay away! We don\'t take outsiders!',
                 'Delphine: Askeladd! It\'s me Delphine! We need help!',
                 'Askeladd: Delphine?'
                 ]

    read_dialogue(dialogue1, 5)
    loading(4)
    read_dialogue(dialogue2, 5)
    loading(4)

    dialogue3 = ['* Delphine had good relations with the town elder Askeladd *',
                 '* Because of this the refugees and I were welcomed with open arms *',
                 '* While the refugees made their acquaintances with the villagers, Askeladd asked to speak '
                 'specifically with me in private. . . *'
                 ]

    dialogue4 = ['Lucy: ' + user_name + '?',
                 'Delphine: Yes how strange. . . Askeladd can I ask why you ask for this person?',
                 'Askeladd: It is none of your business! It is all part of the greater destiny!',
                 '* I am wondering if this old man is just insane. . . *',
                 'Lucy: erm-',
                 '* Delphine takes a long deep sigh *',
                 'Delphine: We can trust him Lucy, even if he is a bit crazy in the head. . .',
                 ]

    dialogue5 = ['"Why me?"',
                 'Delphine: Your name is ' + user_name + '? Am I correct?',
                 'Delphine: ' + user_name + '. . I am unsure myself but don\'t worry, the old man for the most part is'
                                            ' harmless',
                 'Delphine: If you don\'t know already, old man Askeladd is a sage, he has the ability to read '
                 'people\'s soul',
                 '"You didn\'t answer my question. Why me?"',
                 'Delphine: I am quite unsure myself also why he asked for you. . ',
                 'Delphine: I don\'t seem to recall you when we lead the refugees into the cave. . .',
                 'Delphine: Well Askeladd is going to get mad the longer we wait. .',
                 'Delphine: Go ' + user_name + '. You\'ll find your answers with him. . .'
                 ]

    read_dialogue(dialogue3, 5)
    loading(4)
    read_dialogue(dialogue4, 5)
    loading(4)
    read_dialogue(dialogue5, 5)
    loading(4)

    dialogue6 = ['* I made my way to Askeladd\'s hut, a shabby yet humble place built with rusty wood *\n',
                 'Askeladd: Sit down already!',
                 '"Yes sir. . "',
                 'Askeladd: The prophecy foretold of a being whose smell reeked of dragon\'s feet!',
                 '* Yep... This old man is insane...  *',
                 '"Hopefully I don\'t smell that bad to you?"',
                 'Askeladd: No you misunderstand! In Vanaheim, where I come from, it means tha- ',
                 '* Askeladd then went on about his homeland and then goes off topic with many other subjects. . *',
                 ]

    dialogue7 = ['Askeladd: I\'m going off topic!',
                 '"You think?!"',
                 'Askeladd: Anyways! I\'m here to read your soul!',
                 '"Why though?"',
                 'Askeladd: I see that your soul is intertwined with the greater plan!',
                 '"Greater plan, greater destiny, the prophecy. . What are you going on about?!',
                 'Askeladd: Hush child!',
                 '* Before I knew it, he had gently placed his hand on my head *',
                 '* It was then that I saw that I was not in the physical realm anymore *',
                 '* Darkness that blanketed my world, then flashes of exuberant light. . *',
                 '* I had to close my eyes. . After the flashing stopped, I reopened them. . *',
                 '* I was in a field of blue flowers, in front of me stood a lone yet beautiful red flower. . *',
                 ]

    read_dialogue(dialogue6, 5)
    loading(5)
    read_dialogue(dialogue7, 5)
    loading(3)

    choice = user_choice('Touch the red flower',
                         'Crush the red flower',
                         'Smell the red flower',
                         'Don\'t do anything')

    if choice == '1':  # Traits are based off of Cyberpunk 2077 tarot cards
        global traits
        traits = 'the fool'

        dialogue = ['* I touched the red flower *',
                    '* The color of red seeps into my hand *',
                    '* Terrified, I immediately let go of it *',
                    '* As I let go, I touch the blue flowers by accident *',
                    '* The blue flowers turns red, like a plague, the flowers continued to infect themselves with'
                    ' the color red *',
                    '* The field of blue flowers had become red. . *'
                    ]
        read_dialogue(dialogue, 5)

    elif choice == '2':
        traits = 'the devil'

        dialogue = ['* I crushed the red flower *',
                    '* In a world filled with blue, red would only sully it *',
                    '* I had purified this world from the abominated flower *',
                    '* However, without red, blue had seep too deep within this world *',
                    '* As far as I looked, there were no other color besides blue *',
                    '* For some reason, I had felt incredibly lonely . . *',
                    '* This field of blue flowers had turned me mad. . *'
                    ]
        read_dialogue(dialogue, 5)

    elif choice == '3':
        traits = 'temperance'

        dialogue = ['* I smell the red flower *',
                    '* A unique smell that I was not able to describe with words *',
                    '* But somehow. . I came to an understanding after smelling this red flower *',
                    '* In this world, the red flower had kept the balance *',
                    '* Knowing this, I decide to leave the world as it was. . *'
                    ]
        read_dialogue(dialogue, 5)

    elif choice == '4':
        traits = 'the moon'

        dialogue = ['* I decided not to do anything *',
                    '* It is the most logical choice, as I do not know anything as of right now *',
                    '* This world that I inhabit. . *',
                    '* Is it real. . or is it an illusion? *'
                    ]
        read_dialogue(dialogue, 5)


# Chapter 5 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def stormfell_castle():
    loading(5)

    dialogue1 = ['* I gasped, I awoken from that dream *',
                 '* I\'m back at Askeladd\'s hut. . *',
                 '* Askeladd is no where to be seen though. . *',
                 '* I hear a commotion outside the hut *',
                 '* I decide to go outside and see what\'s going on. . *',
                 ]
    read_dialogue(dialogue1, 4)
    loading(4)

    dialogue2 = ['Delphine: ' + user_name + '! You\'re coming with me! We\'re going to Stormfell Castle!',
                 '"Wait what for?! I just woke up!"',
                 'Delphine: I\'ll explain on our way!',
                 '* Delphine picks me up, carries me, and throws me on her horse, what immense strength! *',
                 'Horse: Neeeeiggghhhh!',
                 'Delphine: Off we go!'
                 ]
    read_dialogue(dialogue2, 4)
    loading(4)
    completion_of_level('Chapter 5: Stormfell Castle')
    loading(4)

    dialogue3 = ['* As we made our way to Stormfell Castle, Delphine explained the situation *',
                 '* It had so seemed that Askeladd had caught the attention of the Academy *',
                 '* A group of sages that was under direct control of king Godfrey, which as of of currently'
                 ' lays in the hands of queen Melania *',
                 '"What does the Academy want with Askeladd? And why are we going to Stormfell instead?"',
                 'Delphine: Long story short, Askeladd knows more than those old geezers want him to know. .',
                 'Delphine: And as for Stormfell, I am requesting backup! We are going to take the Academy by storm!',
                 '"Doesn\'t this imply a revolt against the queen?!"',
                 'Delphine: Yes! I plan on a revolution!',
                 '"Holy crap. . ."',
                 '* I am surrounded by insane people! *'
                 ]
    read_dialogue(dialogue3, 5)
    loading(7)

    dialogue4 = ['"We made it to Stormfell castle, it is smaller than I thought.."',
                 'Delphine: Its me! Delphine! Open up the gates!',
                 ]
    dialogue5 = ['"No one\'s opening it up. . "',
                 'Delphine: Hm.',
                 'Delphine: Hey! Open it up! Is anyone in there?!'
                 ]

    dialogue6 = ['Delphine: You\'re right ' + user_name + '. . How strange. .',
                 'Delphine: Have any idea what to do?'
                 ]
    read_dialogue(dialogue4, 4)
    loading(4)
    read_dialogue(dialogue5, 4)
    loading(4)
    read_dialogue(dialogue6, 4)

    choice = user_choice('Yell louder',
                         'Break through the gate with your fist',
                         'Check if there are any other entrances',
                         'Cast a fireball and destroy the gate')
    gate_choices(choice)


def gate_choices(choice):
    if choice == '1':
        dialogue1 = ['* You decide that you just need to yell louder *',
                     '"HEY! IS ANYONE IN THERE?!"'
                     ]
        dialogue2 = ['"No one is here. . ."',
                     'Delphine: Hm. We\'ll just have to get in through force.'
                     ]

        read_dialogue(dialogue1, 4)
        loading(4)
        read_dialogue(dialogue2, 4)
        delphine_gate_lines()

    elif choice == '2':
        if user_character.physical_lvl > 0:
            user_character.physical_lvl += 1

            dialogue = ['* You break through the gate with your fist! *',
                        'Delphine: Woah. . .',
                        '"Well what are you waiting for? Lets go!"',
                        'Delphine: Yes! Let us go!',
                        'Delphine: I hope nothing bad has happened to this place. . .',
                        '* Delphine whispers *',
                        'Delphine: I hope nothing has happened to David. .'
                        ]
            read_dialogue(dialogue, 4)
        else:
            dialogue = ['* You punch the gate, however it does nothing. . *',
                        'Delphine: Good try! Let me have a go at it. . '
                        ]
            read_dialogue(dialogue, 4)
            delphine_gate_lines()

    elif choice == '3':
        if pet == 'Kon':
            global weapon
            weapon = 'steel sword'

            dialogue1 = ['* You try to find another entrance but to no avail *',
                         '* You are about to give up until mist begin forming beneath your feet *',
                         '* A fox the size of a husky emerges! *',
                         'Delphine: Kon?!',
                         '"Oh right! This is Lucy\'s summon!"',
                         '* The fox seems to know of a way to get inside. .  *'
                         ]

            dialogue2 = ['* We found a secret entrance *',
                         '"How does Kon know?"',
                         'Delphine: A lot of summons have different abilities. .',
                         'Delphine: Kon for one has the ability of seeing transparently',
                         '"Nice!"'
                         ]

            dialogue3 = ['* We found a secret room *',
                         '* There was a steel sword so I took it *',
                         'Delphine: Hope that sword suits you well!',
                         '* We make our way up to the main castle *',
                         'Delphine: I hope nothing bad has happened to this place. .',
                         '* Delphine whispers *',
                         'Delphine: I hope nothing has happened to David. .'
                         ]
            read_dialogue(dialogue1, 5)
            loading(3)
            read_dialogue(dialogue2, 5)
            loading(3)
            read_dialogue(dialogue3, 5)

        else:
            dialogue = ['* You try to find the another entrance but to no avail *',
                        'Delphine: Hm. We\'ll just have to get in through force.'
                        ]
            read_dialogue(dialogue, 4)
            delphine_gate_lines()

    elif choice == '4':
        if user_character.magic_lvl > 0:
            user_character.magic_lvl += 1

            dialogue1 = ['\n* You decide to cast a fireball *',
                         '* You think long and hard about how Victor did it *',
                         '* After a while a orb of fire emits from your stick *',
                         '* You focus even harder, the orb of fire grows bigger! *',
                         '* Delphine looks at you with surprise *',
                         '* ~Sweeeessshhhhh~ ~ You fire at the gate! *',
                         '* BAMMMMMMM *',
                         '* The gate is now opened *',
                         '\nDelphine: Holy crap, I didn\'t know you were a mage!',
                         '"Is it really all that surprising?"',
                         'Delphine: Yes it is! Mages are rare around these parts!'
                         ]

            dialogue2 = ['Delphine: Alright enough chit chat, it\'s time to check the Castle!',
                         'Delphine: I hope nothing bad has happened to this place. . .',
                         '* Delphine whispers *',
                         'Delphine: I hope nothing has happened to David. .'
                         ]

            read_dialogue(dialogue1, 5)
            loading(3)
            read_dialogue(dialogue2, 4)

        else:

            dialogue = ['* You try to cast a fireball, however you don\'t know how to! *',
                        'Delphine: For a second I thought you were a mage!',
                        'Delphine: Let me try to have a go at it'
                        ]
            read_dialogue(dialogue, 4)
            delphine_gate_lines()


def delphine_gate_lines():
    dialogue1 = ['* Delphine unsheathes her sword *',
                 '* She prays, her sword starts to glow *',
                 'Delphine: Argh!',
                 '* Her sword slices through the gate with ease! *',
                 '"Woah. . What was that?',
                 'Delphine: You mean my sword art?',
                 '"Yes. ."',
                 'Delphine: Ah, its a technique held from way up North',
                 'Delphine: North God Style, a sacred technique that was passed to me from my master',
                 '"Oh wow, can I learn it?"',
                 'Delphine: Haha I am sorry but I cannot, I am not a great teacher',
                 '"Ah I see. . "',
                 'Delphine: However if you go the Capital, maybe you can find my mentor and he can teach you!']
    dialogue2 = ['Delphine: Alright enough chit chat, it\'s time to check the Castle!',
                 'Delphine: I hope nothing bad has happened to this place. . .',
                 '* Delphine whispers *',
                 'Delphine: I hope nothing has happened to David. .'
                 ]
    read_dialogue(dialogue1, 5)
    loading(2)
    read_dialogue(dialogue2, 4)


# Chapter 6 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def the_lover():
    loading(5)
    completion_of_level('Chapter 6: The Lovers')
    loading(5)

    dialogue1 = ['* I think I heard Delphine muttered the name "David". . *',
                 '* I wonder if he is someone special to her *',
                 '* We searched through the castle *',
                 '* It was barren empty, not a single life form roamed in here *',
                 '\n"Are you sure we got the right place?"',
                 'Delphine: Yes, I would never forget the place I met David. . ',
                 '"David?"',
                 'Delphine: Yes, my lover. . ',
                 '* I decided not to pry into it any further *',
                 '"Ah I see. . "'
                 ]

    dialogue2 = ['* We continued to search within the castle *',
                 '* Delphine began to become noticeable irritated *',
                 '\nDelphine: Let\'s check David\'s room.',
                 '"Alright"',
                 '\n* We made it to David\'s room *',
                 '* If I had to tell by the look of David\'s room, I would have guess that he was of knightly order'
                 ]

    dialogue3 = ['Delphine: He was the one who saved me. . .',
                 'Delphine: Before I was an adventurer, I came from the countryside. . ',
                 'Delphine: It was a beautiful place west of here. .',
                 'Delphine: However the Baron of Whiterun had fancied me, and took me away. . ',
                 'Delphine: For years I was a servant to the Baron. . Until one day. . ',
                 'Delphine: David rescued me. . .',
                 '"I see. ."'
                 ]

    dialogue4 = ['Delphine: This castle belongs to only myself and David. . ',
                 '"Wait what about the back up?"',
                 'Delphine: That was David. .',
                 '"Wha- Where is he now then?"',
                 'Delphine: I too am confused by his absence. .',
                 '\n* We search through David\'s room if we could find anything of relevance *',
                 '* There was a note that was left behind *',
                 '* It was by the Academy. . . *',
                 '\nDelphine: D*mn those conniving sages!',
                 'Delphine: D*mn it! We have to go to the Academy now! We can\'t wait a minute longer!'
                 ]
    read_dialogue(dialogue1, 5)
    loading(3)
    read_dialogue(dialogue2, 5)
    loading(3)
    read_dialogue(dialogue3, 5)
    loading(3)
    read_dialogue(dialogue4, 5)

    choice = user_choice('"Then lets go!"',
                         '"Wait isn\'t this too brash?"',
                         '"I\'m with you!"',
                         '"We should think about this more carefully!"')

    if choice == '1':
        npc_delphine.favour += 1
        print("I had reassured Delphine with my help, we set off to the Academy!")
    elif choice == '2':
        print("* She promptly ignored me, picked me up, and we had set off to the Academy! *")
    elif choice == '3':
        npc_delphine.favour += 1
        print("I had reassured Delphine with my help, we set off to the Academy!")
    elif choice == '4':
        print("* She promptly ignored me, picked me up, and we had set off to the Academy! *")
    loading(5)


# Chapter 7 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def the_academy():
    completion_of_level('Chapter 7: The Academy')
    loading(5)

    dialogue1 = ['* Our journey was long and treacherous, meeting bandits and wolves along the way *',
                 '* However we eventually made it to the Academy *',
                 '* It was made almost entirely of marble, with grand statues of heroes and sages alike *',
                 '* It had grand water fountains and lush greenness that were planted around its campus *',
                 '* It was a beautiful place, one that screamed of its prestige and illustriousness *'
                 ]

    dialogue2 = ['\nDelphine: Ugh. . I told myself at one point in time that I would never go here again. . ',
                 'Delphine: Those sages with their all high mightiness. . Ugh. . Thinking about it grosses me out',
                 'Delphine: No matter. We\'re getting David and that hermit Askeladd back!'
                 ]

    dialogue3 = ['\n* We arrived at the front entrance *',
                 '* It was grand. . It was if it had reached up to heaven. . *',
                 '"Um. . How exactly are we suppose to open this?"',
                 'Delphine: Just wait. . '
                 ]

    dialogue4 = ['\nDoor: Who dares enter the The Grand Palace of Alexandria!',
                 '"Holy crap! The door just spoke now!"',
                 'Delphine: Delphine and ' + user_name + ' wish to enter!',
                 'Door: I see. . ',
                 'Door: A soul of fiery passion, and another with a soul of . .'
                 ]
    read_dialogue(dialogue1, 5)
    read_dialogue(dialogue2, 5)
    read_dialogue(dialogue3, 5)
    loading(4)
    read_dialogue(dialogue4, 5)

    if traits == 'temperance':
        print("Door: temperance. . .")
        loading(2)
        print('"Temperance?"')

    elif traits == 'the fool':
        print("Door: a fool. . .")
        loading(2)
        print('"A fool?"')

    elif traits == 'the devil':
        print("Door: a devil. . .")
        loading(2)
        print('"A devil?"')

    elif traits == 'the moon':
        print("Door: the moon. . .")
        loading(2)
        print('"The moon?"')

    loading(4)

    dialogue5 = ['Delphine: Strange. . .',
                 'Delphine: The door went silent when it spoke of your soul. . ',
                 '\n* Before I could told her my soul, the door had opened. .  *',
                 '* Great winds howled and pushed Delphine and I back. . *',
                 '* After couple seconds it had ceased *',
                 '\nDoor: You may enter. . .'
                 ]
    read_dialogue(dialogue5, 5)
    loading(5)


# Chapter 8 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def the_great_debate():
    completion_of_level('Chapter 8: The Great Debate')
    loading(5)

    dialogue1 = ['\n* We entered the so called "palace" *',
                 '* We were met by an old scholar *\n'
                 'Scholar 1: We have awaited you Delphine!',
                 'Scholar 1: And who is this you brought along?',
                 'Delphine: The prophecy\'s very own chosen. .',
                 'Scholar 1: I knew that already. . Their name?',
                 '"Name\'s ' + user_name + '."',
                 'Scholar 1: ' + user_name + '. . How interesting. .',
                 'Scholar 1: Well then ' + user_name + '. Let us make haste.',
                 'Scholar 1: The council is expecting you two.'
                 ]

    dialogue2 = ['\n* We made our way through the long and grandiose corridors of the palace *',
                 '* I could not help be but amazed at the architecture *\n',
                 'Scholar 1: It is only natural you are filled with wonder',
                 'Scholar 1: The Palace of Alexandria was made in Alexandria\'s own image.',
                 '"This Alexandria person is a too bit into themselves. ."',
                 'Scholar 1: How ignorant! I\'ll let you kno-',
                 '* Another scholar appeared *',
                 'Scholar 2: What is this commotion about? Cease with your imprudence! The council is waiting inside'
                 ' as we speak.',
                 'Scholar 1: My apologizes brother. . I had not seen we were already here. . ',
                 '\n* We were greet with grand door. . carved in it was a frowning face. . *\n'
                 ]

    dialogue3 = ['Door: What is the wisdom of the red flower. . ',
                 'Scholar 2: For there is no peace without chaos. .',
                 'Door: What is the wisdom of the blue flower. .',
                 'Scholar 1: For there is no chaos without peace. .',
                 'Door: He. . He. . He. He. He. He.He.',
                 '\n* I must be imagining it, but it the door smiling? *',
                 '* A creepy and devilish smile overtook the door. . *\n',
                 'Door: You may enter. . .'
                 ]

    dialogue4 = ['Delphine: That door always gave me the creeps. .',
                 '"That\'s understandable. ."',
                 '\n* We entered a room with dozens of sages waiting for us *',
                 '* From the right I had saw Askeladd and David *',
                 'Delphine: David!',
                 'David: Delphine!',
                 'Scholar 3: Silence!',
                 'Scholar 3: We had expected you arrival. . .',
                 'Scholar 3: We can now begin the debate!'
                 ]
    read_dialogue(dialogue1, 5)
    loading(3)
    read_dialogue(dialogue2, 5)
    loading(3)
    read_dialogue(dialogue3, 5)
    loading(3)
    read_dialogue(dialogue4, 5)
    loading(7)


start_game()
cave_level()
the_state_of_the_world()
to_solitude()
the_hermit()
stormfell_castle()
the_lover()
the_academy()
the_great_debate()
print("\nPart One - Completed")
