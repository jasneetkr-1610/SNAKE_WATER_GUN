import random
import time
from colorama import init,Fore,Style

init(autoreset=True)

print(Fore.MAGENTA+"------------------SNAKE - WATER - GUN  GAME----------------- ")
print()
print(Fore.CYAN+"RULES OF THE GAME :")
print()
print(Fore.YELLOW+"1. SNAKE  drinks WATER --> SNAKE WINS")
print(Fore.YELLOW+"2. WATER  drouses GUN --> WATER WINS")
print(Fore.YELLOW+"3. GUN  kills SNAKE --> GUN WINS")
print()
print()
time.sleep(3)

player_name=input("Please Enter your NAME:")
print()
print(Fore.BLUE+f"------------------WELCOME {player_name}-----------------")
choices=['snake','water','gun']
player_score=0
computer_score=0

for round_no in range(1,6):
    print(Fore.BLUE+f"ROUND NO:{round_no}")
    print()
    player_choice=input(Fore.CYAN+"Enter your choice (snake/water/gun):").lower()

    while player_choice not in choices:
        print(Fore.RED+"Invalid choice!")
        player_choice=input(Fore.CYAN+"Enter your choice (snake/water/gun):").lower()

    computer_choice=random.choice(choices)
    print()
    print(Fore.MAGENTA+f"Computer Chooses:{computer_choice}")
    print()
    time.sleep(2)

    if player_choice==computer_choice:
        print(Fore.YELLOW+"It's a Tie!")
    elif (player_choice=="snake" and computer_choice=="water") or\
        (player_choice=="water" and computer_choice=="gun") or\
        (player_choice=="gun" and computer_choice=="snake"):
        print(Fore.LIGHTGREEN_EX+f"PLAYER  {player_name} WINS THIS ROUND")
        player_score+=1
    else:
        print(Fore.LIGHTGREEN_EX+"COMPUTER WINS THIS ROUNDS.")
        computer_score+=1
    print("-------------------------------------------------------------")
    print()
    time.sleep(3)
    print(Fore.MAGENTA+f"SCOREBOARD:\n{player_name.upper()}:{player_score}| COMPUTER:{computer_score}")
    print()
    time.sleep(2)

print(Fore.RED+"-----------------------GAME OVER---------------------------")
print()
print(Fore.BLUE+f"FINAL RESULTS:")
if player_score>computer_score:
    print(Fore.YELLOW+f"CONGRATULATIONS {player_name.upper()}! YOU WON THE GAME.")
elif computer_score>player_score:
    print(Fore.YELLOW+"COMPUTER WINS THE GAME! BETTER LUCK NEXT TIME.")
else:
    print(Fore.YELLOW+" THE GAME ENDS WITH A TIE!")