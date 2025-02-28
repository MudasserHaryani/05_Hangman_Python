import random
import string

# List of words for the game
words = ['apple', 'banana', 'cherry', 'mango', 'orange', 'kiwi', 'grape', 'lemon', 'peach', 'plum']

# Hangman ASCII art stages (from 0 wrong guesses to 6 wrong guesses)
hangman_stages = [
    """
       --------
       |      |
       |      
       |    
       |      
       |     
    """,
    """
       --------
       |      |
       |      O
       |    
       |      
       |     
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      
       |     
    """,
    """
       --------
       |      |
       |      O
       |     /|
       |      
       |     
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |      
       |     
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / 
       |     
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / \\
       |     
    """
]

def get_valid_word(words):
    """
    Selects a random word from the list that does not contain '-' or ' '.
    Returns the word in uppercase.
    """
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word that need to be guessed
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # letters the user has guessed

    lives = 6

    print("Let's play Hangman!")
    
    # Game loop: Continue until the user guesses the word or runs out of lives
    while len(word_letters) > 0 and lives > 0:
        print(hangman_stages[6 - lives])
        print(f"Lives left: {lives}")
        print("Used letters: ", " ".join(sorted(used_letters)))
        
        # Display current progress of the word (e.g., A - P P - E)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))
        
        user_letter = input("Guess a letter: ").upper().strip()
        
        # Ensure the user enters a single character
        if len(user_letter) != 1:
            print("Please enter a single letter.\n")
            continue
        
        # If the letter is valid and hasn't been guessed
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"Good job! {user_letter} is in the word.\n")
            else:
                lives -= 1
                print(f"Sorry, {user_letter} is not in the word.")
                print(f"You have {lives} lives left.\n")
        elif user_letter in used_letters:
            print("You have already guessed that letter. Try again.\n")
        else:
            print("Invalid character. Please try again.\n")
    
    # End of game: Check if user has guessed the word or lost
    if lives == 0:
        print(hangman_stages[6])
        print(f"Game Over! You lost. The word was: {word}")
    else:
        print(f"Congratulations! You guessed the word {word} correctly.")

# Start the game
hangman()
