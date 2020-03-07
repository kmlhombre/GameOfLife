from random import randint

# basic parameters of map
aliveCellsOnStart = 5
height = 5
width = 5

aliveCells = aliveCellsOnStart


def displayMap(map):
    for x in map:
        print('  '.join(x))


def letsTheGameBegin(map):
    while aliveCells > 0:
        copy_map = initMap()
        for x in range(height):
            for y in range(width):
                aliveNeighbours = 0
                left = 0
                right = width - 1
                if map[x][y] == 'X':
                    if y > 1:
                        left = y-1
                    if y < right - 2:
                        right = y+1
                    if x != 0:
                        for z in range(left, right):
                            if map[x-1][z] == 'O':
                                aliveNeighbours += 1
                    if map[x][left] == 'O':
                        aliveNeighbours += 1
                    if map[x][right] == 'O':
                        aliveNeighbours += 1
                    if x != height - 1:
                        for z in range(left, right):
                            if map[x+1][z] == 'O':
                                aliveNeighbours += 1
                    if aliveNeighbours == 3:
                        copy_map[x][y] = 'O'
                aliveNeighbours = 0
                if map[x][y] == 'O':
                    if y > 1:
                        left = y-1
                    if y < right - 1:
                        right = y+1
                    if x != 0:
                        for z in range(left, right):
                            if map[x - 1][z] == 'O':
                                aliveNeighbours += 1
                    if map[x][left] == 'O':
                        aliveNeighbours += 1
                    if map[x][right] == 'O':
                        aliveNeighbours += 1
                    if x != height - 1:
                        for z in range(left, right):
                            if map[x + 1][z] == 'O':
                                aliveNeighbours += 1
                    if aliveNeighbours == 2 or aliveNeighbours == 3:
                        copy_map[x][y] = 'O'
        map = copy_map
        displayMap(map)
        print('--------------------------')
        control = input()
        if control == 's':
            break


def initMap():
    map = []
    for _ in range(height):
        record = []
        for _ in range(width):
            record.append('X')
        map.append(record)
    return map


def initGame():
    # init dead map
    map = initMap()

    # add alive cells
    for _ in range(aliveCellsOnStart):
        while True:
            number = randint(0, 24)
            if map[int(number/5)][number%5] == 'X':
                map[int(number/5)][number%5] = 'O'
                break

    # display initial map
    displayMap(map)
    print('--------------------------')

    letsTheGameBegin(map)


if __name__ == '__main__':
    initGame()