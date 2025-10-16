import random
import os

print("Welcome to Cricket by Darsh")

print("Let's have a toss!\n1. Heads\n2. Tails")
toss_choice = 0
try:
    toss_choice = int(input("Your choice: "))
except ValueError:
    print("Invalid Input. Please enter a number.")
play_choice = 0
runs = 0
comp_runs = 0
inning = 0

if toss_choice == random.randint(1, 2):
    inning = 1
    print("You win!")
    print("Would you like to bat or bowl?\n1. Bat\n2. Bowl")
    play_choice = int(input("Your choice: "))
else:
    inning = 1
    print("You couldn't win the toss.")
    if random.randint(1, 2) == 1:
        print("You have to bat.")
        play_choice = 1
    else:
        print("You have to bowl.")
        play_choice = 2

while play_choice == 1:
    shot = int(input("Enter your shot (1 to 6): "))
    comp_choice = random.randint(1, 6)
    print(f"Computer played {comp_choice}")
    if shot == comp_choice:
        print(f"That's your wicket!\nYou set the target of {runs + 1}")
        inning = 2
        print("That's the end of 1st Inning!\nGet ready for 2nd Inning!")
        input("Press Enter to continue..")
        os.system("clear")
        break
    else:
        runs += shot

while play_choice == 2:
    ball = int(input("Enter your ball (1 to 6): "))
    comp_bat = random.randint(1, 6)
    print(f"Computer played {comp_bat}")
    if ball == comp_bat:
        print(f"You got him!\nComputer scored {comp_runs}")
        inning = 2
        print("That's the end of 1st Inning!\nGet ready for 2nd Inning!")
        input("Press Enter to continue..")
        os.system("clear")
        break
    else:
        comp_runs += comp_bat

if inning == 2:
    if play_choice == 1:
        print("Its your turn to bowl.\nDon't let computer surpass you.")
        comp_runs = 0
        while comp_runs <= runs:
            ball = int(input("Enter your ball (1 to 6): "))
            comp_bat = random.randint(1, 6)
            print(f"Computer played {comp_bat}")
            if ball == comp_bat:
                print(f"You got him!\nComputer scored {comp_runs}")
                print("You WIN!!")
                break
            else:
                comp_runs += comp_bat
            if comp_runs > runs:
                print("You lose...")
                print(
                    f"Computer managed to score {comp_runs} runs while you scored {runs}."
                )
    if play_choice == 2:
        print("Its your turn to bat.\nTrick your opponent to win!")
        runs = 0
        while runs <= comp_runs:
            shot = int(input("Enter your shot (1 to 6): "))
            comp_choice = random.randint(1, 6)
            print(f"Computer played {comp_choice}")
            if shot == comp_choice:
                print("That's your wicket!")
                print(f"You made {runs} runs.")
                print("You lose!")
                break
            else:
                runs += shot
            if runs > comp_runs:
                print("You played fabulous...\nYou WIN!!")
