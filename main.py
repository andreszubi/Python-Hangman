import random

# Set up the stages of the hangman game with the ASCII art.
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Set up the word list for the hangman game.
word_list = ["aardvark", "baboon", "camel"]

# Set up the lives for the hangman game.
lives = 6

# Choose a random word from the word list.
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
    # Get the guess from the user.
    guess = input("Guess a letter: ").lower()
    display = ""
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
    if guess not in display:
        lives -= 1
        print(f"You have {lives} lives left.")
        #Check if the user has lost the game.
        if lives == 0:
            game_over = True
            print(stages[0])
            print("You guessed:")
            print(display)
            print(f"The word was: {chosen_word}.")
            print("You lose!")
            break

    # Check if the user has won the game.
    if "_" not in display:
        game_over = True
        # Print the stage left of the hangman game.
        if lives == 6:
            print(stages[6])
        elif lives == 5:
            print(stages[5])
        elif lives == 4:
            print(stages[4])
        elif lives == 3:
            print(stages[3])
        elif lives == 2:
            print(stages[2])
        elif lives == 1:
            print(stages[1])
        print("You guessed:")
        print(display)
        print(f"The word was: {chosen_word}.")
        print("You win!")
        break
    # Print the ASCII art for the hangman game.
    if lives ==  6:
        print(stages[6])
        print("Guessed so far:")
        print(display)
    elif lives == 5:
        print(stages[5])
        print("Guessed so far:")
        print(display)
    elif lives == 4:
        print(stages[4])
        print("Guessed so far:")
        print(display)
    elif lives == 3:
        print(stages[3])
        print("Guessed so far:")
        print(display)
    elif lives == 2:
        print(stages[2])
        print("Guessed so far:")
        print(display)
    elif lives == 1:
        print(stages[1])
        print("Guessed so far:")
        print(display)



