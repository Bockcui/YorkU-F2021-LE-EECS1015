# Lab 3
# Author: Cheng Tian Cui
# Email: cttcui@my.yorku.ca
# Student ID: 218082305
# Section A

#Task 1
print("\n--- Task 1 ---: Compute Fare")

task1a = ""
task1b = ""
fare = "Total amount due: $"

oneWay = 1.80
roundTrip = 3.50
cost = 0

print("(1) One way or (2) round trip?")
while not (task1a == "1" or task1a == "2"):
    task1a = input("Enter 1 or 2: ").strip()

print("Select Age Group:\n(1) Under 12\n(2) 13-64\n(3) 65 or older")
while not (task1b == "1" or task1b == "2" or task1b == "3"):
    task1b = input("Enter 1, 2, or 3: ").strip()

if task1a == "1" and task1b == "2":
    cost = oneWay
elif task1a == "1" and (task1b == "1" or task1b == "3"):
    cost = oneWay / 2
elif task1a == "2" and task1b == "2":
    cost = roundTrip
elif task1a == "2" and (task1b == "1" or task1b == "3"):
    cost = roundTrip / 2

fare = fare + "{:.2f}".format(cost) + " ["

if task1a == "1":
    fare = fare + "one way  ("
elif task1a == "2":
    fare = fare + "round trip  ("

if task1b == "2":
    fare = fare + "full fare)]"
elif task1b == "1" or task1b == "3":
    fare = fare + "reduced fare)]"

print(fare)

#Task 2
print("\n--- Task 2 ---: Parse string")

task2 = input("Input a string: ")
task2r = ""

for i in range(0,len(task2)):
    if task2[i] == " ":
        print("str[" + str(i) + "] = SPACE")
    else:
        print("str[" + str(i) + "] = " + task2[i])

for j in range(len(task2) - 1, -1, -1):
    if task2[j] != " ":
        task2r = task2r + task2[j]

print("Reverse no spaces: " + task2r)

#Task 3
print("\n--- Task 3 ---: The maximum *even* number")

maxeven = 0
task3 = 0

print("Keep entering positive integer\nTo quit, input a negative integer")

while not task3 < 0:
    task3 = int(input("Enter a number: "))

    if (task3 % 2) == 0 and task3 > maxeven:
        maxeven = task3

print("Largest even number: " + str(maxeven))

#Task 4
print("\n--- Task 4 ---: Better triangle draw")

task4 = 0

while not (task4 >= 5 and task4 <= 20):
    task4 = int(input("Enter size between 5 and 20: "))

for i in range(0,task4,1):
    print(i*"-" + "\\")

print(task4 * "-" + "|")

for j in range(task4 - 1, -1,-1):
    print(j * "-" + "/")