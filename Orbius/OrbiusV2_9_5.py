# TO DO LIST
# - Add a system to check for numerics in input
# - Add more responses to the answer pools 
# - Move on already...

# importing required modules
import random, time, gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf

YesPool = [
        "'tis certain m'lord.",
        "I would deem it most probable, sire.",
        "Does a bear shit in the woods, sire?.",
        "If this is deemed to be false, then I would sooner eat my hat m'lord.",
        "You may rely upon it.",
        "Yay, sire.",
        "But, of course my 'lege.",
        "As the children of the time say 'frfr, ong, no cap', cryptic have the contemporary youth become.",
        "Yes."
        ]
MaybePool = [
        "Reply hazy, try again.",
        "Shoo! I'm far too busy at this time.",
        "Well I simply couldn't spoil the surprise.",
        "The orb is cloudy, not much can be seen.",
        "*CRSHASHS* Fuck! You broke the orb.",
        "The stars are not in position! Stars! Can't do it. Not today.",
        "I forgor 💀💀💀 ",
        "*shrugs*",
        "Who's to say?"
        ]
NoPool = [
        "If that were true, sire, then St. George himself would come down from the heavens to kiss upon thine slippers.",
        "Nay, m'lord",
        "My sources say no.",
        "Sire, have you been into the mead again?",
        "I give you my sincerest doubts my liege.",
        "Do pigs fly? No sire, no they do not.",
        "Please sire, don't ask such silly questions, you're smarter than that.",
        "No."
        ]

class Orbius(Gtk.Window):
    def __init__(self):
        # determining the title, border, and size of the window
        Gtk.Window.__init__(self, title="Orbius v2.9.5")
        self.set_border_width(5)
        self.set_size_request(600, 200)

        # creating the greeting label, response box, and answer label, and query button (widgets)
        greeting_label = Gtk.Label(label="Give your query to the magic orb?")
        self.raw_input_label = Gtk.Entry()
        self.answer_label = Gtk.Label(label="")
        query_button = Gtk.Button(label="Query")
        query_button.connect("clicked", self.on_query_button_clicked)

        # creating the box to hold the widgets
        OrbiusBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        OrbiusBox.pack_start(greeting_label, False, False, 10)
        OrbiusBox.pack_start(self.raw_input_label, False, False, 0)
        OrbiusBox.pack_start(query_button, False, False, 0)
        OrbiusBox.pack_start(self.answer_label, False, False, 10)
        self.add(OrbiusBox)

    # validates user input and if valid, proceeds
    def on_query_button_clicked(self, widget):

        # this grabs the user's input to validate
        raw_input = self.raw_input_label.get_text()

        # this checks whether or not there actually is a response, if not it gives a message
        if raw_input.strip() == "":
            self.answer_label.set_text("Please submit a 'yes or no' query.")
        
        else:
            # this checks if the input is too long by counting the characters
            # if the count is too high it gives a message
            raw_input_value = len(raw_input.strip())
            if raw_input_value > 10: ## placeholder value
                self.answer_label.set_text("Your query is too long.")

            ## &^^^& needs a numerics checking system

            else:
                # generates a "random" integer from 0 to 6
                # portions of 7(0-6)| 2:3:2 | 30%:40%:30%
                Orbsight = random.randint(0, 6) 
                if Orbsight <= 1:
                    answer = random.choice(YesPool)   
                if Orbsight >= 5: 
                    answer = random.choice(NoPool)
                else:
                    answer = random.choice(MaybePool)
                
                # to keep an eye on things :eyes:
                print("Debugging values:")
                print(raw_input.strip())
                print(Orbsight)
                print(answer)

                # updates the response with generated answer
                self.answer_label.set_text(answer)



win = Orbius()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
