import numpy as np

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 8, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2]]


# grid = [[5, 0, 0, 0, 1, 0, 0, 0, 4],
#         [2, 7, 4, 0, 0, 0, 6, 0, 0],
#         [0, 8, 0, 9, 0, 4, 0, 0, 0],
#         [8, 1, 0, 4, 6, 0, 3, 0, 2],
#         [0, 0, 2, 0, 3, 0, 1, 0, 0],
#         [7, 0, 6, 0, 9, 1, 0, 5, 8],
#         [0, 0, 0, 5, 0, 3, 0, 1, 0],
#         [0, 0, 5, 0, 0, 0, 9, 2, 7],
#         [1, 0, 0, 0, 2, 0, 0, 0, 3]]

# print(np.matrix(grid))


def possible(y, x, n):
    global grid
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
    if x == y:
        for i in range(0, 9):
            if grid[i][i] == n:
                return False
        if x ==4 and n !=5:
            return False
    if x == 8-y:
        for i in range(0, 9):
            if grid[i][8-i] == n:
                return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
    input('More?')


solve()
