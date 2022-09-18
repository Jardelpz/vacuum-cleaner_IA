# Questions
# A) A sua solução é extensível para um mundo 3 x 3? E para um mundo 6 x 6? Explique sua resposta.
#   Sim, pois se desde que haja espaço a ser analisado, o robo ira funcionar

# B) É possível ter todo o espaço limpo efetivamente? Justifique sua resposta.
#   Sim, pois uma vez que mapeamos o ponto sujo, conseguimos caminhar até chegar nele e
#   contabilizar se a quantidade de pontos sujos são iguais aos pontos sujos já limpos pelo robo.


import sys

import matplotlib.pyplot as plt
from random import randint

victory = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1]]

rows = 6
columns = 6

def create_board():
    v = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    for r in range(rows):
        for c in range(columns):
            if r == 0 or c == 0 or r == rows - 1 or c == columns - 1:
                v[r][c] = 1

    count = 0
    while count < 3:
        c_aux = randint(1, columns - 2)
        r_aux = randint(1, rows - 2)
        if v[r_aux][c_aux] == 0:
            count += 1
            v[r_aux][c_aux] = 2

    return v


def actions(action, r, c):
    actions = {"down": {"c": 0, "r": 1}, "up": {"c": 0, "r": -1}, "left": {"c": -1, "r": 0}, "right": {"c": 1, "r": 0}, "noop": {"c": 0, "r": 0}, "aspire": {"c": 0, "r": 0}}
    r += actions.get(action).get('r')
    c += actions.get(action).get('c')
    print(f"state of perception: 0 chosen action: {action}")

    return (r, c)


def get_dirty_spaces(board):
    dirty_spaces = []
    for r in range(1, rows - 1):
        for c in range(1, columns - 1):
            if board[c][r] == 2:
                dirty_spaces.append((c, r))

    return dirty_spaces


def should_clean(current_pos, dirty_space):
    return current_pos == dirty_space


def choose_next_movement(current_pos, dirty_space):
    current_r, current_c = current_pos
    dirty_r, dirty_c = dirty_space
    next_move = None
    if current_c < dirty_c:
        next_move = actions("right", current_r, current_c)
    elif current_c > dirty_c:
        next_move = actions("left", current_r, current_c)

    elif current_r < dirty_r:
        next_move = actions("down", current_r, current_c)
    elif current_r > dirty_r:
        next_move = actions("up", current_r, current_c)

    return next_move


def show(matriz):
    pos_r = 1
    pos_c = 1
    count_cleaned = 0
    points = 0

    def refresh_board(matriz):
        plt.imshow(matriz, 'gray')
        plt.nipy_spectral()
        plt.pause(0.4)

    plt.clf()
    plt.plot([pos_c], [pos_r], marker='o', color='r', ls='')
    refresh_board(matriz)

    dirty_space = get_nearest_dirty(matriz, (pos_r, pos_c))
    while dirty_space:
        if should_clean((pos_r, pos_c), dirty_space):
            matriz[pos_r][pos_c] = 0
            refresh_board(matriz)
            count_cleaned += 1
            points += 1
            print("state of perception: 1 chosen action: aspire")
            if count_cleaned == 3:
                matriz = victory
                refresh_board(matriz)
                plt.pause(0.5)
                print(f"Points: {points}")
                sys.exit()

        else:
            next_move = choose_next_movement((pos_r, pos_c), dirty_space)
            points += 1
            pos_r, pos_c = next_move
            plt.clf()
            plt.plot([pos_c], [pos_r], marker='o', color='r', ls='')
            refresh_board(matriz)

        dirty_space = get_nearest_dirty(matriz, (pos_r, pos_c))

    plt.show(block=False)
    plt.clf()


def get_sum_of_distance(dirty_spaces, current_pos):
    sum_of_dirty = {}
    for d_pos in dirty_spaces:
        d_r = 0
        d_c = 0
        if d_pos[0] > current_pos[0]:
            d_r = d_pos[0] - current_pos[0]
        else:
            d_r = current_pos[0] - d_pos[0]

        if d_pos[1] > current_pos[1]:
            d_c = d_pos[1] - current_pos[1]
        else:
            d_c = current_pos[1] - d_pos[1]

        sum_of_dirty[d_pos] = d_r + d_c

    return sum_of_dirty


def get_nearest_dirty(board, current_pos):
    """
    Responsavel por somar a diferenca entre linha e coluna de cada local sujo, e retornar o mais proximo do posicao atual do aspirador
    """
    dirty_spaces = get_dirty_spaces(board)
    next_target = None
    if dirty_spaces:
        sum_of_dirty = get_sum_of_distance(dirty_spaces, current_pos)
        for k, v in sum_of_dirty.items():
            if not next_target:
                next_target = (k, v)
            else:
                if v < next_target[1]:
                    next_target = (k, v)

    return next_target[0]


def check_obj(board):
    for r in range(1, rows - 1):
        for c in range(1, columns - 1):
            if board[c][r] == 2:
                return 1

    return 0


show(create_board())

