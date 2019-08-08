#
# Author: Damber Adhikari
#

#dice.py
import dice 
import random

print("""Petals Around the Rose
--------------------------

The name of the game is 'Petals Around the Rose'. The name of the
game is important. The computer will roll five dice and ask you to
guess the score for the roll. The score will always be zero or an
even number. Your mission, should you choose to accept it, is to
work out how the computer calculates the score. If you succeed in
working out the secret and guess correctly five times in a row, you
become a Potentate of the Rose.\n""")

play = ''
count = 1
correct = 0
wrong = 0
ncount = 0
die_count = [0,0,0,0,0,0,0]
index = 1
correct5count = 0
wrong5count = 0
guesscount = 0


def score():
    global count,correct,wrong,die_count,correct5count,wrong5count,guesscount

    # Generate random number from 1-6 for 5 dices.
    die1 = random.randint(1,6)
    die_count[die1] = die_count[die1] + 1
    die2 = random.randint(1,6)
    die_count[die2] = die_count[die2] + 1
    die3 = random.randint(1,6)
    die_count[die3] = die_count[die3] + 1
    die4 = random.randint(1,6)
    die_count[die4] = die_count[die4] + 1
    die5 = random.randint(1,6)
    die_count[die5] = die_count[die5] + 1

    # Displays the dices from dice.py
    dice.display_dice(die1,die2,die3,die4,die5)

    # Ask the user to input there guess.
    guess = int(input('Please enter your guess for the roll: '))

    # stores value for die's to callculate answer.
    score1 = 0
    score2 = 0
    score3 = 0
    score4 = 0
    score5 = 0

    # Finds out if die's value = 3 or 5 and if they do equal to that change it to 2 and 4 and stores it in score variable.
    if die1 == 3:
        score1 += 2
    elif die1 == 5:
        score1 += 4
    else:
        score1 += 0

    if die2 == 3:
        score2 += 2
    elif die2 == 5:
        score2 += 4
    else:
        score2 += 0

    if die3 == 3:
        score3 += 2
    elif die3 == 5:
        score3 += 4
    else:
        score3 += 0

    if die4 == 3:
        score4 += 2
    elif die4 == 5:
        score4 += 4
    else:
        score4 += 0

    if die5 == 3:
        score5 += 2
    elif die5 == 5:
        score5 += 4
    else:
        score5 += 0

    # Sums the total of die's which are stored in score variable.
    tol = score1+score2+score3+score4+score5

    # Checinking if user input is correct.
    if guess == tol:
        print ("\nWell done! You guessed it!")
        correct = correct + 1
        correct5count = correct5count + 1
    else:
        # If user does not get 5 wrong in a row value of wrong5count is changed to 0.
        correct5count = 0

    # Finding if user input odd number.
    if guess % 2:
        print ("\nNo sorry, it's",tol,'not', guess,"The score is always even.")
        wrong = wrong + 1
        wrong5count = wrong5count +1

    # If user guess does not equal to the total.
    if guess != tol:
        print ("\nNo sorry, it's",tol ,"not",end=' ',)
        print (guess,'.',sep='')
        wrong = wrong + 1
        wrong5count = wrong5count +1
    else:
        # If user does not get 5 wrong in a row value of wrong5count is changed to 0.
        wrong5count = 0

    # If user answer 5 times correctly in row this is printed.
    if  correct5count == 5:
        print()
        print ("\nCongratulations! You have worked out the secret!")
        print ("Make sure you don't tell anyone!")
    # If users answer 5 times wrong this is printed.
    elif wrong5count == 5:
        print()
        print("\nHint: The name of the game is important... Petals Around the Rose.")


# This does not need to be in loop because it is ONLY asked once.
play = input('Would you like to play Petals Around the Rose [y|n]? ')

# If play input does not equal 'y' or 'n', ask them to re enter (loops till user enter 'y' or 'n').
while play != 'y' and play != 'n':
  print ("\nPlease enter either 'y' or 'n'.")
  play = input("\nRoll dice again [y|n]?")

# While play is used so i can create if play == ' n' and stuff.
while play == 'y':
    score()
    print()
    play = input("\nRoll dice again [y|n]? ")
    
    # If user play input = 'n'.
    if play == 'n':
        ncount = ncount +1

if ncount == 0:
  # This is using ncount Variable so it is only displayed if user enters 'n'
    print ()
    print ('\nNo worries... another time perhaps... :)')

# If user press 'n' at the start of the game, the summary is not displayed but if user input 'n' after guessing once it displays summary.    
if ncount >= 1:
    print ()
    print ("\nGame Summary")
    print ("===========\n")
    print ("You played", count, "games:")
    print ("|--> Number of correct guesses: ",'',correct)
    print ("|--> Number of incorrect guesses:",wrong,'\n')
    print()

    print ("Dice Roll Stats:\n")
    print ("Face Frequency")

    # Based on sudocode provided ( if index(1) is less than die_count)
    while index < len(die_count):                                                 
        print ('  ',index,end=' ')
        for number in range(0,die_count[index]):
            print("*",end=' ')
        index = index + 1
        print ('')

    print ("\nThanks for playing!")


