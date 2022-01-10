import random

def task0():
    print('Midterm Exam - EECS1015')
    print('Name: XX')
    print('Student ID: XX')
    print('email: XX')
    print('Section X')

def task1():
    print('\n----------Task 1-----------')

    fname = input('Your first name: ').strip().title()
    lname = input('Your last name: ').strip().upper()

    deposit = ''
    balance = -1.0

    while balance < 0:
        deposit = input('Initial funds to invest: $').strip()

        try:
            balance = float(deposit)
        except ValueError:
            balance = -1.0

    interest = ''
    interestF = ''

    while type(interestF) is not float:
        interest = input('Annual return percentage: ').strip()

        try:
            interestF = 1 + float(interest)/100
        except ValueError:
            interestF = ''

    print(f'Yearly return for {fname} {lname}')
    print(f'Initial deposit: {balance:.2f}')

    for i in range(1,6):
        balance *= interestF
        print(f'Year {i}: {balance:.2f}')

def task2():
    print('\n----------Task 2-----------')
    print('Soda Vending Machine')

    balance = 0.0
    cost = 1.00

    while balance < cost:
        print(f'Current amount ${balance:.2f} out of ${cost:.2f}')
        print('Insert Coin')
        print('1. Toonie  ($2.00)')
        print('2. Loonie  ($1.00)')
        print('3. Quarter ($0.25)')
        print('4. Dime    ($0.10)')
        print('5. Nickel  ($0.05)')
        choice = input('Selection [1-5]? ').strip()

        try:
            coin = int(choice)

            if coin == 1:
                balance += 2.00
            elif coin == 2:
                balance += 1.00
            elif coin == 3:
                balance += 0.25
            elif coin == 4:
                balance += 0.10
            elif coin == 5:
                balance += 0.05
            else:
                print('Invalid selection!')

        except ValueError:
            print('Invalid selection!')

    print(f'Total amount provided: ${balance:.2f}')
    print('Thank you for your purchase.')

    change = balance - cost

    print(f'Please take your change ${change:.2f}')

def task3():
    print('\n----------Task 3-----------')

    play = True
    goal = 35

    while play:
        print('Dice Game')
        print('Rolling Die 10 times')

        rolls = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

        for i in range(1,11):
            roll = random.randint(1,6)
            rolls[roll] += 1
            print(f'Roll {i}: [{roll}]')

        sum = 1 * rolls[1] + 2 * rolls[2] + 3 * rolls[3] + 4 * rolls[4] + 5 * rolls[5] + 6 * rolls[6]

        if rolls[1] == 2:
            print('+10 Bonus for snake eyes [1][1]!')
            sum += 10

        if sum > goal:
            print(f'Total {sum} -- OVER 35 POINTS [YOU WIN!]')
        else:
            print(f'Total {sum} -- TOO FEW POINTS [YOU LOSE!]')

        play = input('Enter \'Y\' to play again: ').strip().upper() == 'Y'

def task4():
    print('\n----------Task 4-----------')
    string = input('Enter string with one word with "quotes": ')

    cases = countCases(string)
    print(f'This string has {cases[0]} uppercase characters.')
    print(f'This string has {cases[1]} lowercase characters.')

    caseflipped = flipCase(string)
    print(f'Case flip: \'{caseflipped}\'')

    quoteslice = cutQuotedText(string)
    print(f'Quote removed: \'{quoteslice}\'')

#Task 4 specified functions
def countCases(string):
    upper = 0
    lower = 0

    for i in range(0, len(string)):
        if string[i].isupper():
            upper += 1
        elif string[i].islower():
            lower += 1

    return [upper, lower]

def flipCase(string):
    newstring = ''

    for i in range(0, len(string)):
        if string[i].isupper():
            newstring += string[i].lower()
        elif string[i].islower():
            newstring += string[i].upper()
        else:
            newstring += string[i]

    return newstring

def cutQuotedText(string):
    if string.count('"') != 2:
        return 'ERROR! No quoted text.'
    else:
        beforequote, quote, afterquote = string.split('"')
        return beforequote + afterquote

#Run tasks in order
task0()
task1()
task2()
task3()
task4()

input('Press enter to exit')
