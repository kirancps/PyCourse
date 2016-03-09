#this function gives the predicted word in game
#logic is to just search the secretword letters in guessed list
#if found, store in a new string, don't bother about index as secretword is iterated
#is the letter in secterword is present in guesed word, store else add '_'


def getGuessedWord(secretWord, lettersGuessed):
    #convert guessed letter into string
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
        


secretWord='apple'
lettersGuessed=['e','b','c','l']

print getGuessedWord(secretWord,lettersGuessed)

