import random
from hangman_words import word_list
from hangman_art import stages, logo



# Set up the lives for the hangman game.
lives = 6

# Choose a random word from the word list.
print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

# Set up the placeholder for the hangman game.
placeholder = ""

# Set up the word length for the hangman game.
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)


# Set up the game over flag for the hangman game.
game_over = False

# Set up the correct letters list for the hangman game.
correct_letters = []

# Set up the while loop for the hangman game.
while not game_over:
    print(f"****************************<{lives}>/6 LIVES LEFT****************************")
    # Get the guess from the user.
    guess = input("Guess a letter: ").lower()
    display = ""

    if guess in correct_letters:
        print(f"You've already guessed the letter '{guess}'. Try a different letter.")
        print(stages[lives])
        continue
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    print(display)

    # Check if the guess is in the chosen word.
    if guess not in chosen_word:
        lives -= 1
        print("You have guessed the letter '{guess}' incorrectly. You have lost a life.")
        print(f"You have {lives} lives left.")
        #Check if the user has lost the game.
        if lives == 0:
            game_over = True
            print(stages[0])
            print("You guessed:")
            print(display)
            print(f"The word was: {chosen_word}.")
            print(f"***********************YOU LOSE**********************")
            break

    # Check if the user has won the game.
    if "_" not in display:
        game_over = True
        # Print the stage left of the hangman game.
        print(stages[lives])
        print("You guessed:")
        print(display)
        print(f"The word was: {chosen_word}.")
        print(f"***********************YOU WIN**********************")
        break
    
    # Print the ASCII art for the hangman game.
    print(stages[lives])
    print("You guessed:")
    print(display)



