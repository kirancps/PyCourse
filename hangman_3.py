
#this function allows the user to get available letters in alphabets which are not yet guesses
#logic is convert the list into string
#check whether alphabet is present in guessed list, if not the store in new var else omit


def getAvailableLetters(lettersGuessed):

    guess=''
    aword=''
    av='abcdefghijklmnopqrstuvwxyz'

    for k in range(len(lettersGuessed)):
        guess+=lettersGuessed[k]


    for i in range(len(av)):

        if not(av[i] in guess):

            aword+=av[i]


    return aword


lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getAvailableLetters(lettersGuessed)

            



    

    
