#Imports
from words import retrieve_word
import re


#Play the game
def play_game():
    currentlyPlaying = True
    inrounds = True
    wordtouse = ""
    currentboard = ""
    currentguessestotal = set()
    currentguesseswrong = set()
    calculatingtemp = ""
    guess = ''
    playagainchoice = ''
    wrongguesscount = 0

    print("Welcome to Hangman!")
    while currentlyPlaying:
        wordtouse = retrieve_word()
        currentboard = re.sub("[a-z]", "_", wordtouse)

        #Begin Rounds
        while inrounds:
            #Show current board and retrieve next guess
            print("Here is the current game board:")
            if wrongguesscount == 0:
                print()
            else:
                print_hang_image(wrongguesscount)
            print_spaced_string(currentboard)
            print("Here is the current letters you have guessed:")
            print_spaced_string(currentguesseswrong)
            guess = get_guess(currentguessestotal)
            print("*****************************************************")

            #Check input character against current board and word
            for x in range(0, len(wordtouse)):
                if wordtouse[x] == guess:
                    calculatingtemp += guess
                elif currentboard[x] != '_':
                    calculatingtemp += currentboard[x]
                else:
                    calculatingtemp += '_'

            #Validate board based on temporary constructed string
            if calculatingtemp == currentboard:
                wrongguesscount += 1
                currentguessestotal.add(guess)
                currentguesseswrong.add(guess)
                print("Sorry that character is not in the word.")

                if wrongguesscount == 7:
                    print_hang_image(wrongguesscount)
                    print("Sorry you are all out of guesses. \nThe word was " + wordtouse + ".")
                    inrounds = False
            else:
                print("The character " + guess + " was in the word.")
                currentguessestotal.add(guess)
                currentboard = calculatingtemp

            #Check if word is completed
            if currentboard == wordtouse:
                print("Congrats! You have successfully guessed the word " + wordtouse + ".")
                inrounds = False

            calculatingtemp = ""

        playagainchoice = input("Would you like to play again? (y/n)")
        #TODO validate input
        if playagainchoice == 'y':
            #Clear out variables to run again
            currentlyPlaying = True
            inrounds = True
            currentguessestotal = set()
            currentguesseswrong = set()
            calculatingtemp = ""
            wrongguesscount = 0
        elif playagainchoice == 'n':
            print("Goodbye")
            currentlyPlaying = False




#Retriece the next guess
def get_guess(currentguessestotal):
    while True:
        guess = input("Please enter your guess:")
        alphavalid = guess.isalpha()
        if alphavalid == False:
            print("Sorry that is not a valid character.")
            continue
        if guess in currentguessestotal:
            print("Sorry, you've already guessed that letter")
            continue
        break
    return guess

#Print out the list with spaces
def print_list(list):
    for item in list:
        print(item, end=" ")
        print()

#Print string with spaces for readibility
def print_spaced_string(word):
    for char in word:
        print(char, end=" ")
    print()


#Prints out the ASCII hangman image
def print_hang_image(count):
        if count == 1:
            print()
            print()
            print()
            print()
            print("___|___")
            print()
        if count == 2:
            print("   |")
            print("   |")
            print("   |")
            print("   |")
            print("   |")
            print("   |")
            print("   |")
            print("___|___")
            print()
        if count == 3:
            print("   ____________")
            print("   |")
            print("   |")
            print("   |")
            print("   |")
            print("   |")
            print("   |")
            print("   |")
            print("___|___")
            print()
        if count == 4:
            print("   ____________")
            print("   |          _|_")
            print("   |         /   \\")
            print("   |        |     |")
            print("   |        |     |")
            print("   |         \\_ _/") 
            print("   |")
            print("   |")
            print("   |")
            print("___|___")
        if count == 5:
            print("   ____________")
            print("   |          _|_")
            print("   |         /   \\")
            print("   |        |     |")
            print("   |         \\_ _/")
            print("   |           |")
            print("   |           |")
            print("   |")
            print("___|___")
        if count == 6:
            print("   ____________")
            print("   |          _|_")
            print("   |         /   \\")
            print("   |        |     |")
            print("   |         \\_ _/")
            print("   |           |")
            print("   |           |")
            print("   |          / \\ ")
            print("___|___      /   \\")
        if count == 7:
            print("   ____________")
            print("   |          _|_")
            print("   |         /   \\")
            print("   |        |     |")
            print("   |         \\_ _/")
            print("   |          _|_")
            print("   |         / | \\")
            print("   |          / \\ ")
            print("___|___      /   \\")


if __name__ == '__main__':
    play_game()



