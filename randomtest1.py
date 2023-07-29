import time
import random


def display(text, delay=2):
    print(text, flush=True)
    time.sleep(delay)

def get_player_choice(prompt, options):
    while True:
        response = input(prompt)
        if response in options:
            return response
        else:
            print("Invalid choice. Please try again.")

def take_gum_out():
    display("You decide to take the gum out of your hair yourself. Now you need to figure out which method of removal you will use.")
    display("Do you want to try using ice cubes or scissors?")
    display("Enter 1 to use ice cubes.\nEnter 2 to use scissors.")
    response = get_player_choice("Your choice: ", ["1", "2"])
    
    if response == "1":
        # Random chance of ice cubes working successfully or not
        if random.choice([True, False]):
            display("You grab a couple of ice cubes from the freezer and gently rub them on the gum stuck in your hair.")
            display("After a few minutes, the gum hardens and becomes easier to remove.")
            display("You successfully remove the gum from your hair without any major mishaps.")
        else:
            display("You grab a couple of ice cubes from the freezer and try to rub them on the gum.")
            display("Unfortunately, the gum seems to become even stickier, making it harder to remove.")
            display("You decide to try another method to remove the gum.")
            # Call another function for the new method
            try_another_method()
    elif response == "2":
        display("You locate a pair of scissors in the bathroom and consider using them to cut the gum out of your hair.")
        display("However, you get a little nervous about the idea of cutting your hair and decide not to go through with it.")
        display("Instead, you opt for a safer method to remove the gum from your hair.")

def try_another_method():
    display("You search for other ways to remove the gum from your hair.")
    display("As you browse the internet, you come across a homemade gum remover recipe using vinegar and baking soda.")
    response = get_player_choice("Enter 1 to try the vinegar and baking soda method.\nEnter 2 to come up with a different plan.\nYour choice: ", ["1", "2"])

    if response == "1":
        display("You mix vinegar and baking soda to create a bubbling concoction.")
        display("Carefully applying it to the gum, you notice the gum starts to break down and lose its stickiness.")
        display("With a little patience and effort, you successfully remove the gum from your hair.")
        display("Congratulations! You've overcome the gum-in-hair crisis with creativity and resourcefulness!")
        # Continue to the original game ending or add a new game ending for this path
    elif response == "2":
        display("You decide that the vinegar and baking soda method doesn't feel right to you.")
        display("Instead, you opt to seek professional help at a nearby salon.")
        display("The stylist at the salon quickly comes to your rescue and safely removes the gum from your hair.")
        display("Phew! Crisis averted thanks to the expert hands of the stylist.")
        # Continue to the original game ending or add a new game ending for this path

def call_mom():
    display("You call your mom, and she suggests using peanut butter to remove the gum or letting her call her favorite stylist to see if she can get you in today.")
    response = get_player_choice("Enter 1 to try using peanut butter.\nEnter 2 to let your mom call the stylist.\nYour choice: ", ["1", "2"])
    if response == "1":
        display("You grab a jar of peanut butter from the kitchen and apply a small amount to the gum.")
        display("To your surprise, the gum loosens and comes out of your hair with ease.")
        display("Your mom's advice turned out to be a lifesaver!")
    elif response == "2":
        display("Your mom calls her favorite stylist, and luckily, the stylist has an open slot today.")
        display("You head over to the stylist, and she skillfully removes the gum from your hair.")
        display("Crisis averted, thanks to your mom's help!")


def game_ending():
    display("With the gum crisis averted, you quickly finish getting ready and head to your office for the meeting.")
    display("As you enter the office, you find your colleagues gathered in the conference room.")
    display("The meeting starts, and you impress everyone with your fabulousness, preparedness, and brilliant ideas.")
    display("Congratulations! You successfully navigated the gum-in-hair emergency and aced your meeting!")
    display("This hairventure may be over for now, but who knows what a different day may bring!")

# Game starts here
display("You awake to the sweet, calming smell of lavender and chamomile. You're still lying in bed.")
display("You're so glad your friend bought that diffuser to help you relax.")
display("You roll over and look at the clock on your nightstand and see it's 10 am.")
display("Wait...You remember your first meeting starts at 12:30pm and it's in person at the office!\n")

display("You quickly jump out of bed, run to the bathroom, and as you are brushing your teeth, you notice something weird in your hair so you lean forward to take a closer look")
display("It's gum!!! You have to take care of this ASAP! Do you try and take it out yourself or call your mom that can always fix your problems?", delay=4)

response = get_player_choice("Enter 1 if you want to take the gum out of your hair yourself.\nEnter 2 if you want to call your mom and see what good advice she can give.\nYour choice: ", ["1", "2"])

# Get players 1st choice (second choice in function)
if response == "1":
    take_gum_out()
elif response == "2":
    call_mom()

# End of game message
game_ending()