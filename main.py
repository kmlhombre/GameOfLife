from random import randint

# basic parameters of map
aliveCellsOnStart = 5
height = 5
width = 5

aliveCells = aliveCellsOnStart


def displayMap(map):
    for x in map:
        print('  '.join(x))


def initGame():
    # init dead map
    map = []
    for _ in range(height):
        record = []
        for _ in range(width):
            record.append('X')
        map.append(record)

    # add alive cells
    for _ in range(aliveCellsOnStart):
        while True:
            number = randint(0, 24)
            if map[int(number/5)][number%5] == 'X':
                map[int(number/5)][number%5] = 'O'
                break

    # display test map
    displayMap(map)


if __name__ == '__main__':
    initGame()