import secrets #using the secrets module for their randomness over the base python functions bc apparently it's slightly better



def QuitFunction(): # defining the "function" to spit out a quit message and keep it looking tidy
    print("Sire, please I beg of you, I simply ~must~ have an audience! NO wait, come back!\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    quit()# it felt odd to define the functions "backwards" to how a human mind would intuitively expect them to flow, cause and effect wise


def TryAgain():#defining a repeat function so that you can ask it multiple questions withoit having to reload the code
    while True:
        raw_responseYorN = input("Would you care to ask me something else?? ('Yes' or 'No')\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n")
        responseYorN = raw_responseYorN.lower()#this converts the input string into lower case letters so that "YES, yes, Yes, yEs, etc." are all valid inputs.
        if responseYorN == "yes":# if yes, it procedes with asking another question
                True_Orbius()
        elif responseYorN == "no":#if no it calls the quit function
                print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
                QuitFunction()
        else:#otherwise it kinda nudges you and tells you you're an idiot, then this function calls itself
            print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n... I beg your pardon sire, I am confused.\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
            TryAgain()

def Corebius():# but it makes sense if you realise that each function needs to be loaded into memory BEFORE it calls it, rather then like constructing it as needed
    GoodVibes = [#answer pools are intentionally shitposty, wanted Orbius to be a time travelling jester-mage type of dude with a magic orb (also lol, morbius)
        "'tis certain m'lord.",
        "I would deem it most probable, sire.",
        "Does a bear shit in the woods, sire?.",
        "If this is deemed to be false, then I would sooner eat my hat m'lord.",
        "You may rely upon it.",
        "Yay, sire.",
        "But, of course my 'lege.",
        "As the children of the time say 'frfr, ong, no cap', cryptic have the contemporary youth become.",
        "Yes."
        ]#Good answer pool ^
    NoVibes = [
        "Reply hazy, try again.",
        "Shoo! I'm far too busy at this time.",
        "Well I simply couldn't spoil the surprise.",
        "The orb is cloudy, not much can be seen.",
        "*CRSHASHS* Fuck! You broke the orb.",
        "The stars are not in position! Stars! Can't do it. Not today.",
        "I forgor 💀💀💀 ",
        "*shrugs*",
        "Who's to say?"
        ]#Neutral Answer pool ^
    BadVibes = [
        "If that were true, sire, then St. George himself would come down from the heavens to kiss upon thine slippers.",
        "Nay, m'lord",
        "My sources say no.",
        "Sire, have you been into the mead again?",
        "I give you my sincerest doubts my liege.",
        "Do pigs fly? No sire, no they do not.",
        "Please sire, don't ask such silly questions, you're smarter than that.",
        "No."
        ]#Bad answer pool^
    Orbsight = secrets.randbelow(7)#generates a random integer from 0 to 6
    print("Debug value", Orbsight) 
    if Orbsight == 7:
        print('ERROR')
    if Orbsight <= 1:#0 or 1
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print(secrets.choice(GoodVibes),"\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        
    elif Orbsight >= 5: # the chances for the pools are done in portions of 7(0-6). 2:3:2 for good, neutral, and bad vibes. in percentages it's very roughly 30%:40%:30%
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print(secrets.choice(BadVibes),"\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")       
    else:# 2,3, or 4
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print(secrets.choice(NoVibes),"\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")

def True_Orbius():#this is the inital question asking part of the code, also validates user input
    while True:
        raw_response = input("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\nAsk the magic 'Orb' something!\n(Type 'No' to exit)\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n")
        try:#this is attempting to convert the initial user input into an integer, if it fails, which it should (cont.)
            raw_response = int(raw_response)#then it will procede, otherwise it will give you a cheeky error message
            print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\nPlease give me words, I'm no good with digits you see.\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        except ValueError:
            break
    raw_response_value = len(raw_response)#this part checks to make sure you didn't ask it anything too "complex"(long), I wanted to give ol' Orbius some character
    if raw_response_value > 30:#arbitrary value of 30(digits, letters, or special characters)
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\nForgive me sire,\nyour query is too great a concern for a lowly fool such as myself to answer.\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        TryAgain()
    response = raw_response.lower()
    if response == "no": #again converting to lowercase to make all variants of "no" valid
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        QuitFunction()
    else:#this is the real meat and potatoes. To make sure you're following, if you ask it a question it will validate your input, then randomly select from 3 pools of responses (cont.)
        Corebius()#then after it's given a response it will loop and let you ask it another question. 
    TryAgain()
    

True_Orbius()#most of the code here is making the program "user proof", because it needs to be usable by a toddler or smth, idfk



# TO DO LIST #
#1.) Make a GUI with PyGObject (HARD)
#2.) Add more responses to the pools (EASY)
#3.) Maybe log the inputs/responses? (UNSURE)
#4.) Move on to a different project (HARD AF)