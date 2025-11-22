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
        if lives == 0:
            game_over = True
            print("You lose.")

    # Check if the user has won the game.
    if "_" not in display:
        game_over = True
        print("You win.")

    # Print the ASCII art for the hangman game.
    



