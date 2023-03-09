## To do list:
# make it save to a file in: 
#   /home/[user]/.security/python_generated_passwords/
# perform input validation 
# make a GUI

## Modules
# os:
# random: for random.choice()
# time:
# string: for string.ascii, etc
# gi: for Gtk
# Gtk: for making a GUI
import os, random, time, string, gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

## defining function
def PasswordGenerator():

    ## assigning necessary characters to a variable
    character_pool = string.ascii_letters + string.digits + string.punctuation
    

    while True:

        ## takes user input for number of passwords
        password_count = int(input("How many passwords to generate?: "))

        while True:

            ## takes user input for length of passwods
            length = int(input("How long should the passwords be?: "))

            ## for each new password created it resets the variable
            for password_index in range(password_count):
                password = ""

                ## then selects a random character x times where x is 'length' 
                # and adds it to the 'password' variable
                for password_length_index in range(length):
                    password = password + random.choice(character_pool)

                ## prints the created password
                # then Ln 37-38 cleans it up
                print("Password generated: ", password)


            return

## function call
PasswordGenerator()
