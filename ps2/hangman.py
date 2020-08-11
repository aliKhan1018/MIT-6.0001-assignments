# Problem Set 2, hangman.py
# Name: Muhammad Ali Khan 
# Collaborators: None
# Time spent: 3hr 30 mins

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    '''
    secret_word = 'apple'
    letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed += letter
        else:
            guessed += '_ '
    return guessed



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    available_alphabets = alphabet
    for letter in alphabet:
        if letter in letters_guessed:
            available_alphabets = available_alphabets.replace(letter, '')
    return available_alphabets
    
    
def deduct_warnings_guesses(warnings, guesses):
    if warnings > 0:
        warnings -= 1
        return warnings, guesses
    elif warnings == 0:
        guesses -= 1
        return warnings, guesses
    elif warnings == 1:
        print('YOU ARE RUNNING OUT OF WARNINGS. GUESSES WILL BE DEDUCTED.')
    return warnings, guesses


def is_vowel(guess):
    VOWELS = 'aeiou'
    if guess not in VOWELS:
        return False
    return True


def number_of_unique_letters(word):
    uniques = []
    for letter in word:
        if letter not in uniques:
            uniques.append(letter)
    return len(uniques)

    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    letters_guessed = []
    warnings = 3

    SEPERATOR = '-'*10

    print('Welcome to hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print(SEPERATOR)
    # main game loop
    while True:
        # End game conditions
        if is_word_guessed(secret_word, letters_guessed):
            print(get_guessed_word(secret_word, letters_guessed))
            print('*** You Win! The word is', secret_word, '***')
            score = guesses * number_of_unique_letters(secret_word)
            print('Your Score is:', score)
            break
        elif guesses <= 0:
            print(f'Sorry. You lose. The word is {secret_word}')
            break
		
		    # Provide info. to player
        print('You Have', warnings, 'warnings left.')
        print('You Have', guesses, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))
        # print the guessed word
        print(get_guessed_word(secret_word, letters_guessed))

		    # Take input as long as the player doesnt input a valid guess
        guess_is_invalid = True
        while guess_is_invalid:
            guess = input('Please guess a letter: ')
            # make sure input is one char
            if len(guess) > 1:
                print('Input must be a character long')
            # if its one char make sure its an alphabet
            elif guess in string.ascii_lowercase:
                guess_is_invalid = False
                # if the guess hasnt been made append it to list
                if guess not in letters_guessed:
                    letters_guessed.append(guess)
                    # deduct guesses depending on the guess being a vowel or a consonant
                    if guess not in secret_word:
                        print('Oops! the letter', guess, 'is not in the word', get_guessed_word(secret_word, letters_guessed))
                        if not is_vowel(guess):
                            guesses -= 1
                        elif is_vowel(guess):
                            guesses -= 2 
                # tell the player that they have already guessed it
                elif guess in letters_guessed:
                    print('You have already guessed letter:', guess)
                    warnings, guesses = deduct_warnings_guesses(warnings, guesses)
                    print('invalid inputs allowed:', warnings)
            # if its none of the above then its an invalid input
            else:
                warnings, guesses = deduct_warnings_guesses(warnings, guesses)
                print('invalid inputs allowed:', warnings)
        print(SEPERATOR)




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(' ', '')
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if not my_word[i] == '_':
                if not my_word[i] == other_word[i]:
                    return False
        return True
    return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
            Keep in mind that in hangman when a letter is guessed, all the positions
            at which that letter occurs in the secret word are revealed.
            Therefore, the hidden letter(_ ) cannot be one of the letters in the word
            that has already been revealed.

    '''
    my_word = my_word.replace(' ', '')
    matches = []
    for word in wordlist:
        is_match = False
        if len(my_word) == len(word):
            for i in range(len(my_word)):
                if not my_word[i] == '_':
                    if not my_word[i] == word[i]:
                        is_match = False
                        break
                    else:
                        is_match = True
        if is_match:
            matches.append(word)
    matches = str(matches).replace('[', '')
    matches = str(matches).replace(']', '')
    matches = str(matches).replace(',', '')
    matches = str(matches).replace("'", '')
    if matches:
        return matches 
    return 'No matches were found'




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    letters_guessed = []
    warnings = 3

    SEPERATOR = '-'*10

    print('Welcome to hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print(SEPERATOR)

    while True:
        # End game conditions
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        if is_word_guessed(secret_word, letters_guessed):
            print(guessed_word)
            print('*** You Win! The word is', secret_word, '***')
            score = guesses * number_of_unique_letters(secret_word)
            print('Your Score is:', score)
            break
        elif guesses <= 0:
            print('Sorry. You lose. The word is', secret_word)
            break
		
        # Provide info. to player
        print('You Have', warnings, 'warnings left.')
        print('You Have', guesses, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))
        # print the guessed word
        print(guessed_word)

        # Take input as long as the player doesnt input a valid guess
        guess_is_invalid = True
        while guess_is_invalid:
            guess = input('Please guess a letter: ')
            # make sure input is one char
            if len(guess) > 1:
                print('Input must be a character long')
            # if its one char make sure its an alphabet
            elif guess == '*':
                print(show_possible_matches(guessed_word))
                print(SEPERATOR)
            elif guess in string.ascii_lowercase:
                guess_is_invalid = False
                # if the guess hasnt been made append it to list
                if guess not in letters_guessed:
                    letters_guessed.append(guess)
                    # deduct guesses depending on the guess being a vowel or a consonant
                    if guess not in secret_word and guess != '*':
                        print('Oops! the letter', guess, 'is not in the word', get_guessed_word(secret_word, letters_guessed))
                        if not is_vowel(guess):
                            guesses -= 1
                        elif is_vowel(guess):
                            guesses -= 2 
                # tell the player that they have already guessed it
                elif guess in letters_guessed:
                    print('You have already guessed letter:', guess)
                    warnings, guesses = deduct_warnings_guesses(warnings, guesses)
                    print('invalid inputs allowed:', warnings)
            # if its none of the above then its an invalid input
            else:
                warnings, guesses = deduct_warnings_guesses(warnings, guesses)
                print('invalid inputs allowed:', warnings)
        print(SEPERATOR)




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
