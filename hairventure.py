import time
import random

# Keeping code dry by creating function to reduce addt'l code lines
def display_slow(text, delay=2):
    print(text, flush=True)
    time.sleep(delay)

# Get player choice and don't let player enter invalid input
def get_player_choice(prompt, options):
    while True:
        response = input(prompt)
        if response in options:
            return response
        else:
            print("Invalid choice. Please try again.") 

# Different game endings based on the player's choices 
def game_ending_successful():
    display_slow("With the gum crisis averted, you quickly finish getting ready and head to your office for the meeting.")
    display_slow("As you enter the office, you find your colleagues gathered in the conference room.")
    display_slow("The meeting starts, and you impress everyone with your fabulousness, preparedness, and brilliant ideas.")
    display_slow("Congratulations! You successfully navigated the gum-in-hair emergency and aced your meeting!")
    display_slow("This hairventure may be over for now, but who knows what a different day may bring!")

def game_ending_unsuccessful():
    display_slow("You call your job and tell them you will not be able to make the meeting.")
    display_slow("A team member jumps in and handles the meeting beautifully.")
    display_slow("Your boss realizes they don't actually need you and you get fired.")
    display_slow("Some stories have nice endings, but not this. Better luck next time!")

def game_ending_successful2():
    display_slow("With the gum crisis temporarily averted, you quickly finish getting ready and head to your office for the meeting.")
    display_slow("As you enter the office, you find your colleagues gathered in the conference room.")
    display_slow("The meeting starts, and you impress everyone with your fabulousness, preparedness, and brilliant ideas.")
    display_slow("You did a superb job at hiding the gum stuck in your hair and no one even noticed!")
    display_slow("Congratulations! You successfully navigated the gum-in-hair emergency and aced your meeting!")
    display_slow("This hairventure may be over for now, but who knows what a different day may bring!")
 
# Give the player choices to make
def take_gum_out():
        display_slow("You decide to take the gum out of your hair yourself. Now you need to figure out which method of removal you will use.")
        display_slow("Do you want to try using ice cubes or scissors?")
        display_slow("Enter 1 to use ice cubes.\nEnter 2 to use scissors.")
        response = get_player_choice("Your choice: ", ["1", "2"])
    
        if response == "1":
        # Give player random chance of ice cubes working successfully or not
            if random.choice([True, False]):
                display_slow("You grab a couple of ice cubes from the freezer and gently rub them on the gum stuck in your hair.")
                display_slow("After a few minutes, the gum hardens and becomes easier to remove.")
                display_slow("You successfully remove the gum from your hair without any major mishaps.")
                game_ending_successful()
            else:
                display_slow("You grab a couple of ice cubes from the freezer and try to rub them on the gum.")
                display_slow("Unfortunately, the gum seems to become even stickier, making it harder to remove.")
                display_slow("You decide to try another method to remove the gum.")
            # Give player option to try something else
                try_another_method()
        elif response == "2":
            if random.choice([True, False]):
                display_slow("You locate a pair of scissors in the bathroom and consider using them to cut the gum out of your hair.")
                display_slow("However, you get a little nervous about the idea of cutting your hair and decide not to go through with it.")
                display_slow("Instead, you choose to style your hair so the gum can't be seen and you'll figure out your next steps after you're finished working for the day.")
                game_ending_successful2()
            else: 
                display_slow("You have no idea what you're doing and you cut more hair than you needed to cut.")
                display_slow("You keep cutting to try and even out your uneven snips.")
                display_slow("Before you know it, you have cut so much that you are at a point of no return.")
                display_slow("You look like a crazy person and there's no way you're leaving the house again until you get a wig or salon appointment.")
                game_ending_unsuccessful()

def try_another_method():
    display_slow("You search for other ways to remove the gum from your hair.")
    display_slow("As you browse the internet, you come across a homemade gum remover recipe using vinegar and baking soda.")
    response = get_player_choice("Enter 1 to try the vinegar and baking soda method.\nEnter 2 to come up with a different plan.\nYour choice: ", ["1", "2"])

    if response == "1":
        display_slow("You mix vinegar and baking soda to create a bubbling concoction.")
        display_slow("Carefully applying it to the gum, you notice the gum starts to break down and lose its stickiness.")
        display_slow("With a little patience and effort, you successfully remove the gum from your hair.")
        display_slow("Congratulations! You've overcome the gum-in-hair crisis with creativity and resourcefulness!")
        game_ending_successful()
    elif response == "2":
        display_slow("You decide that the vinegar and baking soda method doesn't feel right to you.")
        display_slow("Instead, you opt to seek professional help at a nearby salon.")
        display_slow("The stylist at the salon quickly comes to your rescue and safely removes the gum from your hair.")
        display_slow("Phew! Crisis averted thanks to the expert hands of the stylist.")
        game_ending_successful()
#Letting player choose to call mom
def call_mom():
            display_slow("You call your mom, and she suggests using peanut butter to remove the gum or letting her call her favorite stylist to see if she can get you in today.")
            response = get_player_choice("Enter 1 to try using peanut butter.\nEnter 2 to let your mom call the stylist.\nYour choice: ", ["1", "2"])
            if response == "1":
                display_slow("You grab a jar of peanut butter from the kitchen and apply a small amount to the gum.")
                display_slow("To your surprise, the gum loosens and comes out of your hair with ease.")
                display_slow("Your mom's advice turned out to be a lifesaver!")
                game_ending_successful()
            elif response == "2":
                display_slow("Your mom calls her favorite stylist, and luckily, the stylist has an open slot today.")
                display_slow("You head over to the stylist, and she skillfully removes the gum from your hair.")
                display_slow("Crisis averted, thanks to your mom's help!")
                game_ending_successful()

# Need to know if player wants to play again
def play_again():
    return input("Would you like a do over? (yes/no): ").lower() == "yes"

# Need to have game in function to loop if player wants to play again
def main_game():

# Beginning point for game
    display_slow("You awake to the sweet, calming smell of lavender and chamomile. You're still lying in bed.")
    display_slow("You're so glad your friend bought that diffuser to help you relax.")
    display_slow("You roll over and look at the clock on your nightstand and see it's 10 am.")
    display_slow("Wait...You remember your first meeting starts at 12:30pm and it's in person at the office!")
    display_slow("You quickly jump out of bed, run to the bathroom, and as you are brushing your teeth, you notice something weird in your hair so you lean forward to take a closer look")
    display_slow("It's gum!!! You have to take care of this ASAP! Do you try and take it out yourself or call your mom that can always fix your problems?", delay=4)

main_game()

# Game to start over again if player wants to or it stops if the player doesn't want to play again
while True:
    response = get_player_choice("Enter 1 if you want to take the gum out of your hair yourself.\nEnter 2 if you want to call your mom and see what good advice she can give.\nYour choice: ", ["1", "2"])

# Get players 1st choice (second choice in function)
    if response == "1":
        take_gum_out()
    elif response == "2":
        call_mom()

    if not play_again():
        break  # Stop loop if the player chooses not to play again

print("Thanks for playing and may the odds be in your favor when you play again!")



