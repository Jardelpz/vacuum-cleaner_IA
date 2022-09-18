import sys

import matplotlib.pyplot as plt
from random import randint

posAPAy = 1
posAPAx = 1

rows = 6
columns = 6
v = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
count = 0
for r in range(rows):
    for c in range(columns):
        if r == 0 or c == 0 or r == rows - 1 or c == columns - 1:
            v[r][c] = 1

while count < 3:
    c_aux = randint(1, columns - 2)
    r_aux = randint(1, rows - 2)
    if v[r_aux][c_aux] == 0:
        count += 1
        v[r_aux][c_aux] = 2

victory = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]


def exibir(matriz):
    global posAPAx
    global posAPAy
    count_cleaned = 0

    def refresh_board(matriz):
        plt.imshow(matriz, 'gray')
        plt.nipy_spectral()
        plt.pause(0.4)

    for r in range(1, rows - 1):
        if r % 2 == 0:
            start = columns - 2
            end = 0
            step = -1
        else:
            start = 1
            end = columns - 1
            step = 1

        for c in range(start, end, step):
            plt.clf()
            plt.plot([r], [c], marker='o', color='r', ls='')
            refresh_board(matriz)

            if matriz[c][r] == 2:
                matriz[c][r] = 0
                refresh_board(matriz)
                count_cleaned += 1
                if count_cleaned == 3:
                    matriz = victory
                    refresh_board(matriz)
                    plt.pause(0.5)
                    sys.exit()

    plt.show(block=False)
    plt.clf()


exibir(v)