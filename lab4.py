# Lab 4
# Author: Cheng Tian Cui
# Email: cttcui@my.yorku.ca
# Section A
# Student ID: 218082305

#Import modules
import random

#Generate a number between 2 and 14 with uniform distribution
def getCardValue():
    rank = int(random.uniform(0, 1) * 13) + 2
    return rank

#Converts integers (2-14) to a character card rank
def getCardStr(cardValue):
    if cardValue == 2:
        return '2'
    elif cardValue == 3:
        return '3'
    elif cardValue == 4:
        return '4'
    elif cardValue == 5:
        return '5'
    elif cardValue == 6:
        return '6'
    elif cardValue == 7:
        return '7'
    elif cardValue == 8:
        return '8'
    elif cardValue == 9:
        return '9'
    elif cardValue == 10:
        return 'T'
    elif cardValue == 11:
        return 'J'
    elif cardValue == 12:
        return 'Q'
    elif cardValue == 13:
        return 'K'
    elif cardValue == 14:
        return 'A'
    return 'Rank Error'

#Read input for player bet
def getHLGuess():
    #Sentinel
    guess = ''

    while guess not in {'H', 'L'}:
        guess = input('High or Low (H/L)?: ').upper()
    if guess == 'H':
        return 'HIGH'
    elif guess == 'L':
        return 'LOW'
    else:
        return 'Input Error'

#Read input for bet amount
def getBetAmount(maximum):
    #Sentinel
    bet = 0

    while bet not in range(1, maximum + 1):
        #Save string input for conversion to int
        temp = input('Input bet amount (1 to ' + str(maximum) + '): ')

        #Exception handling for non-integer input
        try:
            bet = int(temp)
        except ValueError:
            bet = 0
    return bet

#Determine if player's guess is correct given two cards
def playerGuessCorrect(card1, card2, betType):
    if card2 > card1 and betType == 'HIGH':
        return True
    elif card2 < card1 and betType == 'LOW':
        return True
    else:
        return False

#Game function loops through a specified number of rounds
#Returns a list [points, round]
def playHighLow(points, goal, rounds):
    #Formatting placeholders
    goalFormat = len(str(goal))
    roundsFormat = len(str(rounds))

    for i in range(1, rounds + 1):
        print('\n-------------------------------------')
        print(f'OVERALL POINTS: {points:>{goalFormat}}    ROUND {i:>{roundsFormat}}/{rounds}')

        #Draw card and show it to player
        card1 = getCardValue()
        card1str = getCardStr(card1)
        print(f'First card is [{card1str}]')

        #Read guess
        guess = getHLGuess()

        #Read bet amount
        bet = getBetAmount(points)

        #Draw second card and show it to player
        card2 = getCardValue()
        card2str = getCardStr(card2)
        print(f'Second card is [{card2str}]')

        #Determine if guess is correct
        result = ''
        if playerGuessCorrect(card1, card2, guess):
            result = 'WON'
            points += bet
        else:
            result = 'LOST'
            points -= bet

        #Display results
        print(f'Card1 [{card1str}] Card2 [{card2str}] - You bet \'{guess}\' for {bet} - YOU {result}')

        #Check points win/loss condition
        if points <= 0:
            return [points, i]
        elif points >= goal:
            return [points, i]
    #Default return
    return [points, i]


#----------------GAME STARTS HERE--------------------

#Game specifications
startingPoints = 100
pointGoal = 500
rounds = 10

#Welcome Message
print('--- Welcome to High-Low ---')
print(f'Start with {startingPoints} points. Each round a card will be drawn and shown.')
print('Select whether you think the 2nd card will be Higher or Lower than the 1st card.')
print('Then enter the amount you want to bet.')
print('If you are right, you win the amount you bet, otherwise you lose.')
print(f'Try to make it to {pointGoal} points within {rounds} tries.')

result = playHighLow(startingPoints, pointGoal, rounds)

if result[0] >= pointGoal:
    print('\n---------------WIN--------------------')
    print(f'YOU MADE IT TO *{result[0]}* POINTS IN {result[1]} ROUNDS!')
    print('--------------------------------------')
elif result[0] <= 0:
    print('\n---------------LOSE-------------------')
    print(f'YOU HAVE *{result[0]}* POINTS AFTER {result[1]} ROUNDS!')
    print('--------------------------------------')
elif result[1] >= rounds:
    print('\n---------------LOSE-------------------')
    print(f'YOU ONLY HAVE *{result[0]}* POINTS IN {result[1]} ROUNDS!')
    print('--------------------------------------')

#Input to terminate
input('\nPress enter to quit.')