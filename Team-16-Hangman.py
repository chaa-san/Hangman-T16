import random

print("\n")
chosen_word = input("Player 1, enter a word: ") 
lives = int(input("Player 1, enter number of guesses: "))  # Number of player live's. #lives = 6 
print("\n")


display = []

for letter in chosen_word:
    display.append("_")

print( display)

while lives > 0:  # Check for number of lives
    guess = input("Choose a letter: ").lower()
    if guess not in chosen_word:  # reduce lives in guess not on chosen_word
        lives -= 1
        print("GUESSES LEFT: ", lives)
        print("\n")
    if lives == 0:
        print("You have no more lives try again")
    # If index of letter in word matches the index of display replace display index with letter
    for index, elem in enumerate(chosen_word):
        if elem == guess:
            display[index] = guess
    print(display)
    # When "_" is no longer present in display then player win.
    if "_" not in display:
        lives = 0
        print("Congratulation! You WIN!")
        break

print("The correct word was: ", chosen_word)