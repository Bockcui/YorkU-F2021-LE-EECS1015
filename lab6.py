# Lab 6
# Name: Cheng Tian Cui
# Email: cttcui@my.yorku.ca
# Student ID: 218082305
# Section A

# variables for task 1
dictMenu = {'Fruits': {'Apple': 1.99, 'Banana': 0.59, 'Kiwi': 1.1, 'Grapes': 2.99, 'Pear': 2.15},
            'Drinks': {'Water': 1.0, 'Juice': 3.5, 'Coffee': 1.5, 'Soda': 1.5, 'Tea': 1.25},
            'Dessert': {'Ice Cream': 2.99, 'Pie': 2.5, 'Cake': 2.75},
            'Main Dishes': {'Masala Dosa': 4.25, 'Jianbing': 2.88, 'Falafel': 5.15, 'Pizza': 8.5}}

# variables for task 2
decoder = {80: 'P', 121: 'y', 116: 't', 104: 'h', 111: 'o', 110: 'n', 105: 'i', 115: 's', 99: 'c', 108: 'l', 46: '.',
           32: ' ', 44: ',', 45: '-', 95: '_', 40: '(', 42: '*', 41: ')', 47: '/', 92: '\\', 61: '=', 39: "'", 124: '|',
           96: '`', 58: ':', 59: ';'}
msg1 = [[80, 121, 116, 104, 111, 110], [105, 115], [99, 111, 111, 108, 46]]
msg2 = [[32, 32, 32, 44, 45, 46], [32, 95, 40, 42, 95, 42, 41, 95], [40, 95, 32, 32, 111, 32, 32, 95, 41],
        [32, 32, 47, 32, 111, 32, 92], [32, 40, 95, 47, 32, 92, 95, 41, 32]]
msg3 = [[32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 40], [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 41],
        [32, 32, 32, 32, 32, 95, 95, 46, 46, 45, 45, 45, 46, 46, 95, 95],
        [32, 44, 45, 61, 39, 32, 32, 47, 32, 32, 124, 32, 32, 92, 32, 32, 96, 61, 45, 46],
        [58, 45, 45, 46, 46, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 46, 46, 45, 45, 59],
        [32, 92, 46, 44, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 44, 46, 47]]


def task1():
    for i in dictMenu:
        print(f'----{i}----')
        for j in dictMenu[i].items():
            print(f'${j[1]:.2f}\t{j[0]}')

def task2():
    print('--- Message 1 ----')
    for a in range(0, len(msg1)):
        line = ''
        for b in range(0, len(msg1[a])):
            line += decoder[msg1[a][b]]
        print(line)

    print('--- Message 2 ----')
    for c in range(0, len(msg2)):
        line = ''
        for d in range(0, len(msg2[c])):
            line += decoder[msg2[c][d]]
        print(line)

    print('--- Message 3 ----')
    for e in range(0, len(msg3)):
        line = ''
        for f in range(0, len(msg3[e])):
            line += decoder[msg3[e][f]]
        print(line)

def main():
    print("------ Task 1 ------")
    task1()

    print("------ Task 2 ------")
    task2()

    input('Press enter to finish.')


if __name__ == '__main__':
    main()