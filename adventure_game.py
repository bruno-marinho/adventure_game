import time
import random

def Intro():
    print("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    time.sleep(2)
    print("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.")
    time.sleep(2)
    print("Enter 1 to knock on the door of the house.")
    time.sleep(2)
    print("Enter 2 to knock on the door of the house.")

def house():
    print("You approach the door of the house.")
    print("You are about to knock when the door opens and out steps a dragon. ")
    print("Eep! This is the dragon's house!")
    print("You feel a bit under-prepared for this, what with only having a tiny dagger.")

def cave():
    print("You peer cautiously into the cave.")
    print("It turns out to be only a very small cave.")
    print("Your eye catches a glint of metal behind a rock.")
    print("You have found the magical Sword of Ogoroth!")

def chooseoption1():
    option1 = ""
    while option1 != "1" and option1 != "2":
        option1 = input("What would you like to do" "\nPlease enter 1  or 2 ")
    return option1

    correctoption = random.radint(1,2)
    if option1 == correctoption:
        print("You peer cautiously into the cave.")
        print("It turns out to be only a very small cave.")
        print("Your eye catches a glint of metal behind a rock.")
        print("You have found the magical Sword of Ogoroth!")
        print("You discard your silly old dagger and take the sword with you.")
        print("You walk back out to the field.")
    else:
        print("You approach the door of the house.")
        print("You are about to knock when the door opens and out steps a dragon.")
        print("Eep! This is the dragon's house!")
        print("The dragon attacks you!")
        print("You feel a bit under-prepared for this, what with only having a tiny dagger.")






Intro()
chooseoption1()
