# -'- coding: utf-8 -*-
# codes from https://gist.github.com/steve806/e4986048ca0ea6d8fd2d58c8f3127444
# -'- coding: utf-8 -*-
import sys
import json
from collections import OrderedDict
from random import choice


def check_land_price(map, x, y, direction):
    point = 0
    way = ['U', 'D', 'R', 'L']
    way.remove(direction)

    if x + 1 < 8 and 'R' in way:
        if map[y][x + 1] == '*':
            point = point + 10
    if x - 1 > -1 and 'L' in way:
        if map[y][x - 1] == '*':
            point = point + 10
    if y + 1 < 8 and 'D' in way:
        if map[y + 1][x] == '*':
            point = point + 10
    if y - 1 > -1 and 'U' in way:
        if map[y - 1][x] == '*':
            point = point + 10

    return point


def main():

    data = json.loads(sys.argv[1])
    map = []

    map_string = data['map']
    player = data['me']

    weigh = {'U': 0, 'D': 0, 'L': 0, 'R': 0}
    ground = ['1', '*']

    for i in range(8):
        map.append(list(map_string[8*i:8*i+8]))

    for i in range(8):
        for j in range(8):
            if player == map[j][i]:
                current_x = i
                current_y = j

    if current_x + 1 < 8:
        weigh['R'] = weigh['R'] + 1
        if map[current_y][current_x + 1] == '*':
            weigh['R'] = weigh['R'] + check_land_price(map, current_x + 1, current_y, 'L')
    if current_x - 1 > -1:
        weigh['L'] = weigh['L'] + 1
        if map[current_y][current_x - 1] == '*':
            weigh['L'] = weigh['L'] + check_land_price(map, current_x - 1, current_y, 'R')
    if current_y + 1 < 8:
        weigh['D'] = weigh['D'] + 1
        if map[current_y + 1][current_x] == '*':
            weigh['D'] = weigh['D'] + check_land_price(map, current_x, current_y + 1, 'U')
    if current_y - 1 > -1:
        weigh['U'] = weigh['U'] + 1
        if map[current_y - 1][current_x] == '*':
            weigh['U'] = weigh['U'] + check_land_price(map, current_x, current_y - 1, 'D')

    possible = []

    scores = sorted(weigh.values())
    best_score = scores[-1]

    if weigh['R'] == best_score:
        possible.append('R')
    if weigh['L'] == best_score:
        possible.append('L')
    if weigh['U'] == best_score:
        possible.append('U')
    if weigh['D'] == best_score:
        possible.append('D')

    print(choice(possible))

main()