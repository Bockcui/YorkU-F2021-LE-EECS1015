# Lab 5
# Author: Cheng Tian Cui
# Email: cttcui@my.yorku.ca
# Student ID: 218082305
# Section A

import random
import pyttsx3

#Task 1 Functions
def generateRandomList(l, max):
    randomlist = []
    for i in range(0,l):
        randomlist.append(random.randint(0, max))
    return  randomlist

def computeAverage(lst):
    return sum(lst) / len(lst)

#Task 2 Functions
def stringToCharLst(string):
    return [char for char in string]

def charsToWord(lst):
    lstout = lst.copy()
    charDict = {'1':'one',
               '2':'two',
               '3':'three',
               '4':'four',
               '5':'five',
               '6':'six',
               '7':'seven',
               '8':'eight',
               '9':'nine',
               '0':'zero',
               '-':'dash'}
    for i in range(0,len(lstout)):
        lstout[i] = charDict[lstout[i]]
    return lstout

def combineWordList(lst, divider):
    combined = ''
    k = len(lst)
    for i in range(0, k):
        combined += lst[i]
        if i < k - 1:
            combined += divider
    return combined

def sayWordList(string):
    engine = pyttsx3.init()
    engine.say(string)
    engine.runAndWait()
    del engine

#Task 1
def task1():
    l = int(input('Input list size: '))
    max = int(input('Input max int: '))
    lst = generateRandomList(l, max)
    avg = computeAverage(lst)
    print('Generated list')
    print(lst)
    print(f'Average value = {avg:.4f}')

#Task 2
def task2():
    number = input('Enter phone number as XXX-XXX-XXXX\nType here: ')
    splitstring = stringToCharLst(number)
    wordlist = charsToWord(splitstring)
    print(splitstring)
    print(wordlist)
    print(combineWordList(wordlist, '->'))
    if input("Say word list? (Y/N) ").upper() == 'Y':
        sayWordList(wordlist)

#Main Function
def main():
    print('\n--------- TASK 1: Random List -------------')
    task1()
    print('\n--------- TASK 2: Phone number to text ---')
    task2()
    input('\nPress enter to quit.')

if __name__ == "__main__":
    main()