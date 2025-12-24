import random

attempts = 6

file = open("words.txt", "r")
words = file.read().split()
file.close()

target_word = random.choice(words)
print(target_word)