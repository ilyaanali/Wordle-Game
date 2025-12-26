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
    feedback = [""] * 5
    remaining_letters = list(target_word)

    #First pass to check for green
    for i in range(5):
        if player_guess[i] == target_word[i]:
            feedback[i] = "🟩"  
            remaining_letters[i] = None

    for i in range(5):
        if player_guess[i] in remaining_letters:    
            feedback[i] = "🟨"  # correct letter wrong position
            remaining_letters[remaining_letters.index(player_guess[i])] = None
        else:
            feedback[i] = "⬛"  # letter not in word

    print("".join(feedback))

    # Check for win
    if player_guess == target_word:
        print("Congratulations! You got the word!")
        break

    attempts -= 1
    print(f"You have {attempts} guesses left")

# If out of attempts
if player_guess != target_word:
    print(f"Game over! The word was {target_word}")
