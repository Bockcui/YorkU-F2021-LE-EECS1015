######
#
# Lab 9
# Author: Cheng Tian Cui
# Email: cttcui@my.yorku.ca
# Student ID: 218082305
# Section A
#
####

class MinMaxList:
    def __init__(self, initializeList):
        self.listData = initializeList
        self.listData.sort()

    def insertItem(self, item, printResult = True):
        if item > self.listData[-1]:
            self.listData.append(item)
            if printResult:
                print(f"Item ({item}) inserted at location {len(self.listData) - 1}")
                self.printList()
        else:
            for index, value in enumerate(self.listData):
                if value >= item:
                    self.listData.insert(index, item)
                    break
            if printResult:
                print(f"Item ({item}) inserted at location {index}")
                self.printList()

    def getMin(self):
        value = self.listData[0]
        self.listData.remove(value)
        return value

    def getMax(self):
        value = self.listData[-1]
        self.listData.remove(value)
        return value

    def printList(self):
        print(self.listData)


# Main function is given.
def main():
    aList = MinMaxList([10, 11, 99, 1, 34, 88])
    bList = MinMaxList([88, 0])
    print("Starting aList: ", aList.listData)
    print("Starting bList: ", bList.listData)

    min1 = aList.getMin()
    min2 = bList.getMin()
    print("MinMaxList minimum with aList is %d" % (min1))
    print("MinMaxList minimum with bList is %d" % (min2))

    aList.insertItem(97)
    bList.insertItem(3)
    print("Insert 97 to aList")
    print("Insert 3 to bList")

    max1 = aList.getMax()
    max2 = bList.getMax()
    print("MinMaxList maximum with aList is %d" % (max1))
    print("MinMaxList maximum with bList is %d" % (max2))


if __name__ == "__main__":
    main()