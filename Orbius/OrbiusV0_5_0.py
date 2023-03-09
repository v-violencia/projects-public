# ""ORBIUS"""
import os
import secrets
def Orbius():
    response = input("\nAsk the magic 'Orb' something!\n (Type 'Neigh!' to exit)")
    GoodVibes = [
        "Fosho .",
        "Lol, probably.",
        "Does a bear shit in the woods, sire?.",
        "Surely... Right?",
        "You may rely upon it.",
        "Yes...",
        "But, of course my 'lege.",
        ]
    NoVibes = [
        "Reply hazy, try again.",
        "Shoo! I'm busy at this time.",
        "Well I simply couldn't spoil the surprise.",
        "The orb is cloudy, not much can be seen.",
        "*CRSHASHS* Fuck! You broke the orb.",
        "The stars are not in position! Stars! Can't do it. Not today.",
        "I forgor 💀💀💀 "
        ]
    BadVibes = [
        "HAH! Could you imagine!",
        "Oh, you were serious...Yeah, no. ",
        "My sources say no.",
        "Hmmmm, definitely not.",
        "[X]- Doubt",
        "Do pigs fly?"
        ]
    os.system('clear')
    try:
        float(response)
        print("Please give me words, I'm no good with digits you see.")
    except:
        if response == "Neigh!":
            os.system('clear')
            print("Sire, please I beg of you, I simply ~must~ have an audience!\nNO wait, come back!")
            quit()
        Orbsight = secrets.randbelow(7)
        if Orbsight <= 1:
            print(response)
            print(secrets.choice(GoodVibes), "\n")
        elif Orbsight >= 5:
            print(response)
            print(secrets.choice(BadVibes), "\n")
            
        else:
            print(response)
            print(secrets.choice(NoVibes), "\n")
Orbius()