
import random

# List of 5 predefined words
words = ["python", "apple", "flower", "computer", "school"]

# Randomly select one word
secret_word = random.choice(words)

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the hidden word!")

# Store guessed letters
guessed_letters = []

# Maximum incorrect attempts
max_attempts = 6

# Count incorrect guesses
wrong_attempts = 0

# Game loop
while wrong_attempts < max_attempts:

    # Display the current word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", " ".join(display_word))
    print("Wrong attempts:", wrong_attempts, "/", max_attempts)

    # Check whether the player has won
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word!")
        break

    # Ask the player for a letter
    guess = input("Guess a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter!")
        continue

    # Check duplicate guesses
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Store the guessed letter
    guessed_letters.append(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_attempts += 1
        print("Wrong guess!")

# Check whether the player lost
if wrong_attempts == max_attempts:
    print("\nGame Over! You lost.")
    print("The correct word was:", secret_word)

print("\nThank you for playing Hangman!")
