#Imports random inorder to generate a random word
import random
#Prints out a clue
print("This word is Magical!")
#Function that generates & displays the word the user must guess 
def getGuess():
  #Creates the word to guess in underscores
  blanks = "-" * len(theWord)
  #Sets amount of times a user can guess
  chancesLeft = 10
  #While loop that allows user to guess based off their chances & if the word is correctly guessed
  while chancesLeft > -1 and not blanks == theWord:
    #Print out the length of the word in blanks
    print(blanks)
    #Prints out the amount of chances a user has leftover
    print (str(chancesLeft))
    #Input that allows a user to guess a character
    chance = input("Choose a letter: ")
    #If length of word is 1 letter
    if len(chance) != 1:
      #-this print statement will execute
      print ("Your guess must have exactly one character!")
      #If user guesses a character correctly
    elif chance in theWord:
      #-this print statement will execute
      print ("Correct!")
      #Fills in the missing characters in the word
      blanks = updateBlanks(theWord, blanks, chance)
      #If user guesses incorrectly
    else:
      #-then this print statement will execute
      print ("Try again!")
      #Decrements the users chances, when their guess is incorrect
      chancesLeft -= 1   
      #If a user has no more chances; they lose
  if chancesLeft = 0:
    print ("You lose!!! The word was: " + str(theWord))
  else:
    # Otherwise the user wins
    print ("You won!!! The word was: " + str(theWord))
# Function that updates the blank spaces in the word user needs to guess
def updateBlanks(secret, guessBlanks, recGuess):
  result = ""
  
  for i in range(len(secret)):
    # Checks if character is in the word to guess
    if secret[i] == recGuess:
      # Adds character if guess is correct
      result = result + recGuess           
    else:
      # Keeps blank open if guess is incorrect
      result = result + guessBlanks[i]
      
  return result
# Array of words
words = ["dwarves","fairies","dragon","mermaid","griffin","elves","wizard","goblin","hobbit","angel","demon","kraken"]
# Generates a random word from the array for the user to guees 
theWord = random.choice(words)
getGuess()
