import random
import time


class Snail:
    # ASCII Animation List
    animation = ["__~@", "_~_@", "~__@"]

    def __init__(self, initials):
        assert len(initials) <= 2, "Snail's initials must be 2 characters." #Mistake here, should be len(initials) == 2 for exactly 2 chars in name
        self.name = initials.upper()
        self.speed = random.randint(1, 10)/10
        self.frame = 0
        self.pos = 0

    def move(self):
        self.pos = self.pos + self.speed
        if self.frame == 2:
            self.frame = 0
        else:
            self.frame += 1

    def getIntPos(self):
        return int(self.pos)

    def getName(self):
        return self.name

    def getStr(self):
        pos = self.getIntPos()
        return " " * pos + Snail.animation[self.frame] + " " * (40 - pos) + self.getName()


def getSnailList():
    snails = []
    n = int(input("How many snails are racing? "))
    for i in range(1, n + 1):
        snails.append(Snail(input("Snail " + str(i) + " two initials: ")))
    return snails


def runRace(snails):
    input("Press enter to start race.")
    timestep = 0
    while True:
        timestep += 1
        print(40 * "-" + "Time  " + str(timestep))
        for s in snails:
            print(s.getStr())
            s.move()
        for i in range(0, len(snails)):
            if snails[i].getIntPos() > 39:
                print("Snail " + snails[i].getName() + " WON!")
                return
        time.sleep(0.2)


def main():
    print("Snail Race...")
    play = "Y"
    while play == "Y":
        runRace(getSnailList())
        play = input("Play again (Y)? ").strip().upper()


if __name__ == "__main__":
    main()
