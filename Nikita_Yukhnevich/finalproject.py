import random

class Pixels:
    def __init__(self):
        self.allPixels = [["" for j in range(12)] for i in range(12)]
        for i in range(len(self.allPixels)):
            for j in range(len(self.allPixels[i])):
                self.allPixels[i][j] = "-"

    def printArray(self):
        for i in range(len(self.allPixels)):
            for j in range(len(self.allPixels[i])):
                print(self.allPixels[i][j], end=" ")
            print("")
        print("\n..................................\n")

    def spawn(self):
        x = int(random.random() * len(self.allPixels))
        y = int(random.random() * len(self.allPixels[0]))
        self.allPixels[x][y] = "H"

    def up(self):
        index1 = 0
        index2 = 0

        for i in range(len(self.allPixels)):
            for j in range(len(self.allPixels[i])):
                if self.allPixels[i][j] == "H":
                    index1 = i
                    index2 = j

        self.allPixels[index1][index2] = "-"

        if index1 == 0:
            index1 = len(self.allPixels) - 1
        else:
            index1 = index1 - 1

        self.allPixels[index1][index2] = "H"
        self.printArray()

    def down(self):
        index1 = 0
        index2 = 0

        for i in range(len(self.allPixels)):
            for j in range(len(self.allPixels[i])):
                if self.allPixels[i][j] == "H":
                    index1 = i
                    index2 = j

        self.allPixels[index1][index2] = "-"

        if index1 == len(self.allPixels) - 1:
            index1 = 0
        else:
            index1 = index1 + 1

        self.allPixels[index1][index2] = "H"
        self.printArray()

    def right(self):
        index1 = 0
        index2 = 0

        for i in range(len(self.allPixels)):
            for j in range(len(self.allPixels[i])):
                if self.allPixels[i][j] == "H":
                    index1 = i
                    index2 = j

        self.allPixels[index1][index2] = "-"

        if index2 == len(self.allPixels[index1]) - 1:
            index2 = 0
        else:
            index2 = index2 + 1

        self.allPixels[index1][index2] = "H"
        self.printArray()

    def left(self):
        index1 = 0
        index2 = 0
        for i in range(len(self.allPixels)):
            for j in range(len(self.allPixels[i])):
                if self.allPixels[i][j] == "H": 
                    index1 = i
                    index2 = j
        self.allPixels[index1][index2] = "-"
        if index2 == 0:
            index2 = len(self.allPixels[index1]) - 1        
        else:
            index2 = index2 - 1

        self.allPixels[index1][index2] = "H"
        self.printArray()

    def spawnEnemies(self): #randomly spawn in up to "i" amount of enemies
        for i in range(10):
            x = int(random.random() * len(self.allPixels))
            y = int(random.random() * len(self.allPixels[0]))

            if self.allPixels[x][y] != "H":
                self.allPixels[x][y] = "V"

    def getArray(self): #Returns the entire 2d array
        return self.allPixels


def decider(move, boardOne, score, arr):
    enemyCount = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "V":
                enemyCount += 1

    if move == "w":
        boardOne.up()
    elif move == "s":
        boardOne.down()
    elif move == "d":
        boardOne.right()
    elif move == "a":
        boardOne.left()

    newEnemyCount = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "V":
                newEnemyCount += 1

    if enemyCount > newEnemyCount:
        score += 1

    return score


def main():
    playing = True
    boardOne = Pixels()

    boardOne.spawn()
    boardOne.spawnEnemies()
    boardOne.printArray()

    score = 0

    while playing:
        print("Enter your move ( G to end )")
        move = input()
        print("")

        if move == "G":
            playing = False
            break

        newScore = decider(move, boardOne, score, boardOne.getArray())
        score = newScore

        print("Score: " + str(score) + "\n")


main()