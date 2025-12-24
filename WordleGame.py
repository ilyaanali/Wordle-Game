import random

attempts = 6

# Load and clean the word list
with open("words.txt", "r") as file:
    words = [word.strip().lower() for word in file.readlines()]

target_word = random.choice(words)

while attempts > 0:
    player_guess = input("Enter your 5-letter guess: ").lower().strip()

    # Check length
    if len(player_guess) != 5:
        print("Your guess must be 5 letters long.")
        continue

    # Feedback
    feedback = ""
    for i, letter in enumerate(player_guess):
        if letter == target_word[i]:
            feedback += "🟩"  # correct letter and position
        elif letter in target_word:
            feedback += "🟨"  # correct letter wrong position
        else:
            feedback += "⬛"  # letter not in word

    print(feedback)

    # Check for win
    if player_guess == target_word:
        print("Congratulations! You got the word!")
        break

    attempts -= 1
    print(f"You have {attempts} guesses left")

# If out of attempts
if player_guess != target_word:
    print(f"Game over! The word was {target_word}")
