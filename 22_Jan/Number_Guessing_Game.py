from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

logo = """                                                                
  /\ \ \_   _ _ __ ___ | |__   ___ _ __    / _ \_   _  ___  ___ ___(_)_ __   __ _ 
 /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|  / /_\/ | | |/ _ \/ __/ __| | '_ \ / _` |
/ /\  /| |_| | | | | | | |_) |  __/ |    / /_\| |_| |  __/\__ \__ \ | | | | (_| |
\_\ \/  \__,_|_| |_| |_|_.__/ \___|_|    \____/ \__,_|\___||___/___/_|_| |_|\__, |
                                                                            |___/ """

# Function to check user's guess
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess and returns remaining turns"""
    if user_guess > actual_answer:
        print("Too High.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")
        return turns

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Main game function
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    answer = randint(1, 100)

    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = 0
    while guess != answer:

        print(f"\nYou have {turns} attempts remaining.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            print(f"The correct answer was {answer}.")
            return
        elif guess != answer:
            print("Guess again.")

# Start game
game()
