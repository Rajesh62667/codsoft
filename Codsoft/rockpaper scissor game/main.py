import random
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def play_game():
    choices = ["rock", "paper", "scissor"]

    while True:
        user_score = 0
        computer_score = 0

        print("\n--- Welcome to Rock, Paper, Scissors! ---")

        while user_score < 3 and computer_score < 3:
            print("\nChoices: rock | paper | scissor")
            user_choice = input("Enter your choice: ").lower().strip()

            if user_choice not in choices:
                print(Fore.YELLOW + "Invalid choice. Please choose rock, paper, or scissor.")
                continue

            com_choice = random.choice(choices)
            print(f"Computer chose: {Fore.CYAN}{com_choice}{Fore.RESET}")

            if user_choice == com_choice:
                print(Fore.BLUE + "It's a Tie!")
            elif (user_choice == "rock" and com_choice == "scissor") or \
                 (user_choice == "paper" and com_choice == "rock") or \
                 (user_choice == "scissor" and com_choice == "paper"):
                print(Fore.GREEN + "You win this round!")
                user_score += 1
            else:
                print(Fore.RED + "Computer wins this round!")
                computer_score += 1

            # Print scores
            print(f"Score => {Fore.GREEN}You: {user_score} {Fore.RESET}| {Fore.RED}Computer: {computer_score}")

        # Final Result after the best of 3 series
        if user_score > computer_score:
            print(f"\n{Fore.GREEN}Congratulations! You won the series!")
        else:
            print(f"\n{Fore.RED}Computer wins the series. Better luck next time!")

        play_again = input("\nDo you want to play another series? (yes/no): ").lower().strip()
        if play_again != "yes":
            print(Fore.MAGENTA + "Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
