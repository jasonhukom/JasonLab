# Generated from: Copy of the_seeker_gameproject.ipynb
# Converted at: 2026-09-28T06:54:03.379Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

import os
import time
from getpass import getpass
import sys, tty, termios

os.system('clear')
def loading_animation():
    bars = []
    length = 100
    for i in range(length + 1):
        bar = "[" + "@" * i + "#" * (length - i) + "]"
        bars.append(bar)

    animation = [b for b in bars]

    for i in range(len(animation)):
        time.sleep(0.05)
        print(f"Loading {animation[i]}", end='\r')
    print("\nLoading complete!")

loading_animation()

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

for i in range(5, 0, -1):
    print(end='\r')
    time.sleep(0.5)


def select_location(one, two, three, four, five, six, seven, eight, nine):
    question = True
    while question == True:
        print("one")
        print("two")
        print("three")
        print("four")
        print("five")
        print("six")
        print("seven")
        print("eight")
        print("nine")
        choice = getch()
        return choice
        break



os.system('clear')
title = "The Seeker"
centered_text = title.center(50)

print("S.A.U.C.E.S Contract".center(50))
whoareyou = True
while whoareyou:
    username = input("Name: ")
    company_name = "Secret Agency for Up-and-Coming Entitled Seekers" #S.A.U.C.E.S
    print(f"Company: {company_name}")
    password = getpass("Passkey: ")
    confirm_password = getpass("Confirm Passkey: ")
    whoareyou = False

for i in range(1, 0, -1):
    print(f"You may not leave this company, you must respect the rules of {company_name}. If you see someone fell, died, or disappeared, do not report it. If you do, we will catch you, by signing that contract you understand. You sign this contract without any force, you signed it by your own will and you will follow what this contract say.", end='\r')
    time.sleep(0.01)

os.system('clear')
starting_menu = True
while starting_menu == True:
    print(centered_text)
    print(f"Welcome, {username} you are selected to be our detective today!")
    print("1. Start Missions")
    print("2. Settings")
    print("3. Exit Game")

    choice = input("")

    if choice == '1':
        os.system('clear')
        loading_animation()
        print("Starting game...")
        time.sleep(2)
        starting_menu = False

    elif choice == '2':
        os.system('clear')
        print(company_name.center(50))
        print("1. Change Name")
        print("2. Change Passkey")
        print("3. Back to Main Menu")

        settings_choice = getpass("Options\n")

        if settings_choice == '1':
            new_username = input("Enter new name: ")
            username = new_username
            print("Your Name has been Changed!")
            os.system('clear')
            time.sleep(2)
            starting_menu = True

        elif settings_choice == '2':
            new_password = getpass("Change Passkey: ")
            password = new_password
            print("Passkey updated!")
            os.system('clear')
            time.sleep(2)
            starting_menu = True

        elif settings_choice == '3':
            continue

        else:
            print("Invalid choice! Returning to main menu.")
            continue

    elif choice == '3':
        os.system('clear')
        print("Exiting game...")
        time.sleep(2)
        os.system('clear')
        exit()

    else:
        print("Invalid choice! Please try again.")
        time.sleep(2)

os.system('clear')
print(f"You finally got a job on the {company_name}. You are super excited, you rushed through the lobby to your new office. Some kid was playing some ball in the lobby, but I didn't care. I ran passed them and into my office. It's more smaller and much cramped than you think, seems uncomfortable to you at first but this is what you get, atleast they give you money here. So you shrugs it off, you put your stuff down below your desk, and went out to get a broom to clean your office. Sinced it's super dirty.")
time.sleep(5)
print("Hallway".center(50))
select_location("{username} Office", "Main Lobby", "Janitor Closet", "Cafeteria", "Stairs", "Elevator", "Painting", "Cat", "")
if choice == '1':
    print("You went back to your office, you could't find a broom outside. So you go look for it in your dirty and cramped office.")
    time.sleep(2)
    print("{username} Office".center(50))
    select_location("Hallway", "{username} Stuff", "Old Computer", "Window", "Bed", "Trash Can", "", "", "")
    if choice == '1':
        print("You think that the broom might not be in your office, instead it's outside. So you went back to the hallway")
        time.sleep(2)
        continue
    elif choice == '2':
        print("Your desk is filthy, not like your old office where it's clean. You see some old papers, a half-eaten sandwich, and a coffee mug. You throw them all in the trash can. Your desk now looks much cleaner than previously. But a wind of dust came from the window, you realized that you really need to clean this office.")
        time.sleep(5)
        print("{username} Office".center(50))
        select_location("Hallway", "Old Computer", "Window", "Bed", "Trash Can", "", "", "", "")
        if choice == '1':
            print("The stormdust made you want to find the broom even more, so you went back to the hallway to find it.")
            time.sleep(2)
            continue
        elif choice == '2':
            print("You go to your desk, there is an old computer right there. You're good at computers")
            time.sleep(10)
            print("{username} Office".center(50))
            select_location("Hallway", "Old Computer", "Bed", "Trash Can", "", "", "", "", "")
            if choice == '1':
                print("You think that the broom might not be in your office, instead it's outside. So you went back to the hallway")
                time.sleep(2)
                continue