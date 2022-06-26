#welcome message
name = input('please enter your name:')
print('hi', name, ', welcome to the rock/paper/scissors game')
import random
while True:

    playerchoice = input("Enter a choice ('R' for rock,'P'for paper,'S' for scissors): ")
    possible_actions = ["R", "P", "S"]
    
    CPU_choice = random.choice(possible_actions)
    print(f"\nYou chose {playerchoice}, computer chose {CPU_choice}.\n")
    
    if playerchoice == CPU_choice:
        print(f"Both players selected {playerchoice}. It's a tie!")
    elif playerchoice == "R":
        if CPU_choice == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif playerchoice == "P":
        if CPU_choice == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif playerchoice == "S":
        if CPU_choice == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    elif (not(playerchoice == possible_actions)):
        print("invalid entry please try again")
        continue
    
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break


