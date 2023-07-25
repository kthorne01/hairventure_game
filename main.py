import time

print("You awake to the sweet, calming smell of lavendar and chamomile. You're still lying in bed.")
time.sleep(2)
print("You're so glad your friend bought that diffuser to help you relax.")
time.sleep(2)
print("You roll over and look at the clock on your nightstand and see it's 10am.")
time.sleep(3)
print("Wait...You remember your first meeting starts at 11:00am and it's in person at the office! Jeez, just when you thought you were going to be relaxing!")
print()
time.sleep(2)
print("You quickly jump out of bed, run to the bathroom, and as you are brushing your teeth you notice something weird in your hair so you lean forward to take a closer look")
time.sleep(2)
print("It's gum!!! You have to take care of this ASAP! Do you try and take it out yourself or call your mom that can always fix your problems?")
time.sleep(4)
print()

print("Enter 1 if you want to take the gum out of your hair yourself.")
time.sleep(1)
print("Enter 2 if you want to call your mom and see what good advice she can give.")
time.sleep(1)

valid_input = False
while not valid_input:
    response = input("Please enter 1 or 2: ")

    if response == "1" or response == "2":
        response = int(response)  # Convert the string response to an integer
        valid_input = True
    else:
        print("I don't understand your choice. Please enter 1 or 2.")

# The game will continue here after the player has entered a valid choice.
if response == 1:
    print("You decide to take the gum out of your hair yourself. Now you need to figure out which method of removal you will use.")
elif response == 2:
    print("You call your mom, and she suggests using peanut butter to remove the gum.")

# If the player chose option 1 to take the gum out of their hair themselves.
if response == 1:
    print("Do you want to try using ice cubes or scissors?")
    time.sleep(1)
    print("Enter 1 to use ice cubes.")
    time.sleep(1)
    print("Enter 2 to use scissors.")
    time.sleep(1)

    valid_input = False
    while not valid_input:
        removal_method = input("Please enter 1 or 2: ")

        if removal_method == "1" or removal_method == "2":
            removal_method = int(removal_method)  # Convert the string response to an integer
            valid_input = True
        else:
            print("I don't understand your choice. Please enter 1 or 2.")

    # Continue the game based on the removal method chosen by the player.
    if removal_method == 1:
        print("You grab a couple of ice cubes from the freezer and gently rub them on the gum stuck in your hair.")
        time.sleep(2)
        print("After a few minutes, the gum hardens and becomes easier to remove.")
        time.sleep(2)
        print("You successfully remove the gum from your hair without any major mishaps.")
    elif removal_method == 2:
        print("You locate a pair of scissors in the bathroom and consider using them to cut the gum out of your hair.")
        time.sleep(2)
        print("However, you get a little nervous about the idea of cutting your hair and decide not to go through with it.")
        time.sleep(2)
        print("Instead, you opt for a safer method to remove the gum from your hair and for now you'll just hide the gum.")

# If the player chose option 2 to call their mom for advice.
elif response == 2:
    print("You're a bit skeptical but willing to give it a try.")
    time.sleep(2)
    print("You grab a jar of peanut butter from the kitchen and apply a small amount to the gum.")
    time.sleep(3)
    print("To your surprise, the gum loosens and comes out of your hair with ease.")
    time.sleep(2)
    print("Your mom's advice turned out to be a lifesaver!")

# Continue the game with the aftermath of the gum removal.
print("With the gum crisis averted, you quickly finish getting ready and head to your office for the meeting.")
time.sleep(3)
print("As you enter the office, you find your colleagues gathered in the conference room.")
time.sleep(3)
print("The meeting starts, and you impress everyone with your fabulousness, preparedness, and brilliant ideas.")
time.sleep(3)
print("Congratulations! You successfully navigated the gum-in-hair emergency and aced your meeting!")
time.sleep(2)
print("This hairventure may be over for now, but who knows what a different day may bring!")

# You can add more to the story or offer the player additional choices to extend the game further.
