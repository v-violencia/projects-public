## To do list:
# make it save to a file in directory of choice
#   (currently saves in root directory in preset filename)
# make a GUI
# make input validation
# make output scrambler pre print/write phase
# make "complexity" selection


## Modules
# os: [currently unused]
# random: for random.choice()
# time: [currently unused]
# datetime: for timestamping
# string: for character_pool
# gi: for Gtk
# Gtk: for making a GUI
import os, random, time, datetime, string, gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from datetime import datetime


## takes user input to run
RawBeginResponse = input("[Yes/No] Generate passwords?: ")
# converts to lower case for polish
BeginResponse = RawBeginResponse.lower()

if BeginResponse == "yes":
    ## takes user input to save passwords
    RawSaveResponse = input("[Yes/No] Save in local storage?: ")
    # converts to lower case for polish
    SaveResponse = RawSaveResponse.lower()

    # there was more here originally, this is an intentional stub
    if SaveResponse == "yes":
        pass
    else:
        pass
else:
    print(" - Goodbye")
    quit()

def Again():
    # takes user input to run again
    RawAgainResponse = input("[Yes/No] Generate more passwords?: ")
    # converts to lower case for polish
    AgainResponse = RawAgainResponse.lower()

    if AgainResponse == "yes":
        PasswordGenerator()
    else:
        print(" - Goodbye")
        quit()
    
def PasswordGenerator():
    ## assigning necessary characters to a variable
    character_pool = string.ascii_letters + string.digits + string.punctuation

    while True:
        ## takes user input for number of passwords
        count = int(input(" - How many passwords to generate?: "))

        while True:
            ## takes user input for length of password(s)
            length = int(input(" - How long should the passwords be?: "))

            ## for each password created it resets the variable
            for count_index in range(count):
                password = ""

                ## selects a random character x times, where x is 'length' 
                # and adds it to the 'password' variable
                for length_index in range(length):
                    password = password + random.choice(character_pool)

                ## output block
                # grabs current date and time
                now = str(datetime.now())
                # prints the password(s) with some formatting and a timestamp
                print(" - " + now + "\n[Password {} generated]\n    {}".format(count_index + 1, password))

                if SaveResponse == "yes":
                    # opens the file in append mode
                    file = open("py_passwords.txt", "a")
                    # writes the password(s) with some formatting and timestamp(s)
                    file.write("\n - " + now + "\n[Password {} generated]\n    {}".format(count_index + 1, password))
                    # closes the file, and then makes a confirmation variable
                    file.close()
                    Written = "yes"

            break

        break

    ## checks confirmation variable
    if Written == "yes":
        # and prints message
        print("\n[Successfully written to file]")

    ## runs Again() until prompted to stop
    Again()

## function call to start the program
PasswordGenerator()




