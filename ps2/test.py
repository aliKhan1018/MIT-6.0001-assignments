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

wordlist = load_words()


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
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
