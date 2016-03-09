def isWordGuessed(secretWord, lettersGuessed):

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

secretWord='curry'
lettersGuessed=['c', 'u', 'r', 'y','e']
print isWordGuessed(secretWord, lettersGuessed)


       

        

        

    
