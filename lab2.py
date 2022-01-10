#Task 1
print("\n----Task 1---- BMI Calculator")

name = input("Name: ")
name = name.strip().title()

weight = float(input("Weight (kg): "))

height = float(input("Height (cm): "))
height = height/100

bmi = weight/height**2

task1 = "Name: {a} Weight: {b:.2f} Height [meters]: {c:.2f}  BMI: {d:.2f}"
print(task1.format(a = name, b = weight, c = height, d = bmi))

#Task 2
print("\n----Task 2---- Leetspeak Converter")
normiespeak = input("Type a long string: ")

leetspeak = normiespeak.upper()
leetspeak = leetspeak.replace("T","+")
leetspeak = leetspeak.replace("A","@")
leetspeak = leetspeak.replace("E","3")
leetspeak = leetspeak.replace("I","|")
leetspeak = leetspeak.replace("B","8")
leetspeak = leetspeak.replace("O","0")
leetspeak = leetspeak.replace("C","[")
leetspeak = leetspeak.replace("S","5")

print(leetspeak)

#Task 3
print("\n----Task 3---- Flipping String")
noflip = input("Input a long string: ")
noflip = noflip.upper()

c = len(noflip)
cut = int(c//2)
flip = noflip[cut:] + "|" + noflip[:cut]
mid = noflip[cut]

print("This string is " + str(c) + " characters long. The middle character is \'" + mid + "\'")
print("Flipped String")
print(flip)

#Task 4
print("\n----Task 4---- Multiple numbers")
expression = input("Input numbers to multiply: ")

mpos = expression.find("*")
a = expression[0:mpos].strip()
b = expression[(mpos + 1):].strip()
c = str(int(a) * int(b))

print("Extracted numbers " + a + " " + b)
print(a + " * " + b + " = " + c)

#End prompt
input("Press enter to exit.")
