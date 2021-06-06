import time
import random


villain = random.choice(["dragon", "wicked fairie", "pirate", "troll"])


def print_pause(msg_to_print_pause):
    print(msg_to_print_pause)
    time.sleep(2)


def Intro():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")

    print_pause("Rumor has it that a " + villain +
                " is somewhere around here, and has been terrifying"
                "the nearby village.")

    print_pause("Enter 1 to knock on the door of the house.")

    print_pause("Enter 2 to peer into the cave")
    chooseoption1()


def fight():
    print_pause("You do your best...")
    print_pause("but your dagger is no match for the " + villain + ".")
    print_pause("You have been defeated!")
    endgame()


def fight2():
    print_pause("As the wicked fairie moves to attack,"
                "you unsheath your new sword.")
    print_pause("The Sword of Ogoroth shines brightly in your"
                "hand as you brace yourself for the attack.")
    print_pause("But the " + villain + " takes one look at your"
                "shiny new toy and runs away!")
    print_pause("You have rid the town of the" + villain +
                ".You are victorious!")
    endgame()


def runaway():
    print_pause("You run back into the field."
                "Luckily, you don't seem to have been followed.")
    print_pause("Enter 1 to knock on the door of the house.")
    time.sleep(2)
    print_pause("Enter 2 to peer into the cave")
    chooseoption1()


def runaway2():
    print_pause("You run back into the field."
                "Luckily, you don't seem to have been followed.")
    print_pause("Enter 1 to knock on the door of the house.")
    time.sleep(2)
    print_pause("Enter 2 to peer into the cave")
    chooseoption2()


def choosehouseoption():
    houseoption = ""
    while houseoption != "1" and houseoption != "2":
        houseoption = input("Would you like to (1) fight or (2) run away? ")

    fightoption = 1
    if int(houseoption) == fightoption:
        fight()
    else:
        runaway()


def choosehouseoption2():
    houseoption2 = ""
    while houseoption2 != "1" and houseoption2 != "2":
        houseoption2 = input("Would you like to (1) fight or (2) run away? ")
    fightoption2 = 1
    if int(houseoption2) == fightoption2:
        fight2()
    else:
        runaway2()


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens"
                "and out steps a" + villain + ".")
    print_pause("Eep! This is the dragon's house!")
    print_pause("You feel a bit under-prepared for this,"
                "what with only having a tiny dagger.")
    choosehouseoption()


def house2():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens"
                "and out steps" + villain + ".")
    print_pause("Eep! This is the " + villain + "'s house!")
    print_pause("The wicked" + villain + " you!")
    choosehouseoption2()


def cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger"
                "and take the sword with you.")
    print_pause("You walk back out to the field.")
    print_pause("Enter 1 to knock on the door of the house.")
    time.sleep(2)
    print_pause("Enter 2 to peer into the cave")
    chooseoption2()


def cave2():
    print_pause("You peer cautiously into the cave.")
    print_pause("You've been here before, and gotten all the good stuff."
                "It's just an empty cave now.")
    print_pause("You walk back out to the field.")
    chooseoption2()


def chooseoption1():
    option1 = ""
    while option1 != "1" and option1 != "2":
        option1 = input("What would you like to do" "\nPlease enter 1  or 2 ")

    correctoption = 2
    if int(option1) == correctoption:
        cave()
    else:
        house()


def chooseoption2():
    option2 = ""
    while option2 != "1" and option2 != "2":
        option2 = input("What would you like to do" "\nPlease enter 1  or 2 ")

    correctoption2 = 1
    if int(option2) == correctoption2:
        house2()
    else:
        cave2()


def endgame():
    end = ""
    while end != "y" and end != "n":
        end = input("Would you like to play again? (y/n)")

    newgame = "y"
    if end == newgame:
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        Intro()
    else:
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")


Intro()
