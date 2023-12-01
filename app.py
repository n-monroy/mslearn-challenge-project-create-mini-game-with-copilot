# Create the game logic of the Python minigame 
# Rules:
# - Rock beats scissors.
# - Scissors beat paper.
# - Paper beats rock.
# The interaction in the game will be through the console
# - The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# - At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# - By the end of each round, the player can choose whether to play again.
# - Display the player's score at the end of the game.
# - The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

# Check your work
# Run the minigame on the console with the python app.py command.
# At the prompt, type one of the game options: rock, paper, or scissors.
# The minigame should inform the player whether the player won, lost, or tied with the opponent.
# Choose to continue playing.
# At the prompt, type screen.
# The minigame should inform the player if the option entered by the player is invalid.
# Repeat steps 2 and 4 to play a few rounds and choose not to continue playing.
# Check if the minigame is terminated and if it displays your score, informing you of the number of wins and rounds.

# Importing the random module
import random

# Defining the game function
def game():
    # Defining the list of options
    options = ["rock", "paper", "scissors"]

    # Defining the score variables
    player_score = 0
    cpu_score = 0

    # Defining the game loop
    while True:
        # Defining the CPU choice
        cpu_choice = random.choice(options)

        # Defining the player choice
        player_choice = input("Choose rock, paper or scissors: ").lower()

        # Validating the player choice
        if player_choice not in options:
            print("Invalid option. Try again.")
            continue

        # Defining the game rules
        if player_choice == "rock" and cpu_choice == "scissors":
            print("You won!")
            player_score += 1
        elif player_choice == "paper" and cpu_choice == "rock":
            print("You won!")
            player_score += 1
        elif player_choice == "scissors" and cpu_choice == "paper":
            print("You won!")
            player_score += 1
        elif player_choice == cpu_choice:
            print("Tie!")
        else:
            print("You lost!")
            cpu_score += 1

        # Defining the game loop
        while True:
            # Defining the play again variable
            play_again = input("Do you want to play again? (yes/no): ").lower()

            # Validating the play again variable
            if play_again != "yes" and play_again != "no":
                print("Invalid option. Try again.")
                continue
            else:
                break

        # Defining the game loop
        if play_again == "yes":
            continue
        else:
            break

    # Displaying the final score
    print(f"Your score: {player_score}")
    print(f"CPU score: {cpu_score}")

# Calling the game function
game()

