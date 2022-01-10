import utilities as u
from random import randint as ri
from time import sleep as sleep

def main():
    print("\n--------- Task0: Submission Info       ------------")
    task0()
    print("\n--------- Task1: Rock, Paper, Scissors ------------")
    task1()
    print("\n--------- Task2: Swap List Elements    ------------")
    task2()
    print("\n--------- Task3: Student Info          ------------")
    task3()
    print("\n--------- Task4: Aquarium              ------------")
    task4()
    input("Press enter to quit.")


def task0():
    print('Final Exam - EECS1015')
    print('Name: XX')
    print('Student ID: XX')
    print('Email: XX')
    print('Section X')


def task1():
    print('Rock, Paper, Scissors!')
    play = 'Y'
    while play == 'Y':
        userSelection = ''
        while userSelection not in {'1','2','3'}:
            print('Make your selection...')
            userSelection = input('(1) rock, (2) paper, (3) scissors? ').strip()
            if userSelection not in {'1','2','3'}:
                print('Invalid selection. Try again.')
        computerSelection = ri(1,3)
        printOutcome(int(userSelection), computerSelection)
        play = input('Play again (Y/N)?').strip().upper()


def printOutcome(userSelection, computerSelection):
    choices = {1:'rock', 2:'paper', 3:'scissors'}
    result = {'win':'You win!', 'lose':'HAL wins!', 'tie':'A tie!'}
    rock = {1:'tie', 2:'lose', 3:'win'}
    paper = {1:'win', 2:'tie', 3:'lose'}
    scissors = {1:'lose', 2:'win', 3:'tie'}
    compare = {1:rock, 2:paper, 3:scissors}
    print(f'You: {choices[userSelection]}')
    print(f'HAL: {choices[computerSelection]}')
    print(result[compare[userSelection][computerSelection]])


def task2():
    userInput = input('Input two or more chars separated by spaces: ').strip()
    assert len(userInput) >= 2, 'Must enter two or more characters!'
    charlist = userInput.split(' ')
    print('Initial list')
    print(charlist)
    print(f'String version: \'{"".join(charlist)}\'')
    swapAdjacentElements(charlist)
    print('Modified list')
    print(charlist)
    print(f'String version: \'{"".join(charlist)}\'')


def swapAdjacentElements(alist):
    pairs = len(alist)//2
    for i in range(0, pairs):
        left = alist[2*i]
        right = alist[2*i+1]
        alist[2*i], alist[2*i+1] = right, left


def task3():
    profileList = []
    for id, name in enumerate(u.students):
        profile = [name]
        for key in u.studentsInfo:
            if id in u.studentsInfo[key]:
                profile.append(key)
        profileList.append(tuple(profile))
    profileList.sort()
    for i in profileList:
        print(f'{i[0]:>10s} ({i[1]}) Program: {i[2]} Housing: {i[3]}')


def task4():
    input('Press enter to start aquarium')
    creatures = []
    for i in range(0,5):
        creatures.append(u.SeaLife(ri(0,1),ri(5,30)))
    timestep = 0
    while timestep < 50:
        timestep += 1
        print(40 * '-' + 'Time: ' + str(timestep))
        for j in range(0,5):
            print(creatures[j].getStr())
            creatures[j].move()
        sleep(0.3)


if __name__ == "__main__":
    main()
