# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

secretWord=chooseWord(wordlist)
count=8


#print chooseWord(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

    guess=''
    flag=0
    #converts list to string, you cannot compare list and string
    for i in range(len(lettersGuessed)):

        guess+=lettersGuessed[i]
    #counts the number of similar char i secret and guess word
    for k in range(len(secretWord)):

        if (secretWord[k] in guess):

            flag+=1
            
    #if all the char in secretword is matched with guess word, return true
    if (flag == len(secretWord)):
        return True

    else:

        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guess=''
    gword=''

    for k in range(len(lettersGuessed)):
        guess+=lettersGuessed[k]

    for i in range(len(secretWord)):

        if(secretWord[i] in guess):

            gword+=secretWord[i]+' '
            
        else:
            gword+='_ '

    return gword



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    guess=''
    aword=''
    av='abcdefghijklmnopqrstuvwxyz'

    for k in range(len(lettersGuessed)):
        guess+=lettersGuessed[k]


    for i in range(len(av)):

        if not(av[i] in guess):

            aword+=av[i]


    return aword

    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print (" Welcome to game, Hangman!")
    print ("I am thinking of a word that is "+str(len(secretWord))+" letters long")
    print ("--------------------")
    lettersGuessed=[]   
    count=8

    while (count!=0):

        if(isWordGuessed(secretWord,lettersGuessed)):
           break
        
        
        print("You have " + str(count)+ " guesses left.")

        print ("Available Letters: "+getAvailableLetters(lettersGuessed))

        inSt=raw_input("Please guess a letter : ")
        inStr = inSt.lower()
        

        if not(inStr in lettersGuessed):
           lettersGuessed.append(inStr)

           if (inStr in secretWord ):
               
               print ("Good guess: "+ getGuessedWord(secretWord, lettersGuessed))
           
           else:
               count-=1
               print("Oops! That letter is not in my word: "+ getGuessedWord(secretWord, lettersGuessed))
        else:
           print ("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed))


        print ("-----------------------------------------------------")
        print(" ")

    if count==0:

        print ("Sorry, you ran out of guesses. The word was else. ")
    else :

        print ("Congratulations, you won! ")
           
        

            


        


    




        
        
              

            
       
    
                
        

        



    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
print secretWord
hangman(secretWord)


       



