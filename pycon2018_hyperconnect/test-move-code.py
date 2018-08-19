# -*- coding: utf-8 -*-
# codes from https://gist.github.com/steve806/5349ffa1235e981830ed6397c807e50c
from time import sleep
import sys
import subprocess
import json


def move(player, direction, map):

    for i in range(10):
        for j in range(10):
            if map[i][j] == player:
                prev_x = j
                prev_y = i

    post_x, post_y = prev_x, prev_y
    if direction == 'U':
        post_y = prev_y - 1
    elif direction == 'D':
        post_y = prev_y + 1
    elif direction == 'R':
        post_x = prev_x + 1
    elif direction == 'L':
        post_x = prev_x - 1

    if post_x < 1 or post_x > 8 or post_y < 1 or post_y > 8:
        return False

    if map[post_y][post_x] == '*':
        map[prev_y][prev_x] = player.lower()
        map[post_y][post_x] = player
        return True
    else:
        return False


def check_no_way_to_go(map, player):
    default = False
    post_x = 0
    post_y = 0
    for i in range(10):
        for j in range(10):
            if map[i][j] == player:
                post_x = j
                post_y = i
    if map[post_y][post_x + 1] != '*' and map[post_y][post_x - 1] != '*' and \
       map[post_y + 1][post_x] != '*' and map[post_y - 1][post_x] != '*':
        default = True

    return default


def print_map(map):
    for i in range(8):
        temp_str = ''
        for j in range(8):
            if map[i+1][j+1] == '*':
                temp_str = temp_str + '💎'
            elif map[i+1][j+1] == 'A':
                temp_str = temp_str + '😀'
            elif map[i+1][j+1] == 'a':
                temp_str = temp_str + '👟'
        print(temp_str)


def main():
    f = open("result.txt", 'a')

    file_name_1 = sys.argv[1]

    snake_map = [['0' for x in range(10)] for y in range(10)]
    for i in range(8):
        for j in range(8):
            snake_map[i+1][j+1] = '*'

    direction = ['U', 'D', 'L', 'R']

    A_start_x = 1
    A_start_y = 1

    snake_map[A_start_y][A_start_x] = 'A'

    data1 = {'opponent_history': '', 'my_history': ''}

    A_history = ''
    B_history = ''

    print("===================")
    print_map(snake_map)
    print("===================")
    print("\n")

    while(True):
        input_str = ''
        for i in range(8):
            input_str = input_str + ''.join(snake_map[i+1][1:9])

        data1.update({'map': input_str,
                      'opponent_history': B_history, 'my_history': A_history,
                      'me': 'A', 'opponent': 'B'})

        data_str1 = json.dumps(data1)

        out1 = subprocess.check_output([sys.executable, file_name_1, data_str1]).decode().strip()
        direction1 = str(out1)

        trick = 0
        if direction1 not in direction:
            print("Do not use Trick")
            return

        valid = move('A', direction1, snake_map)
        if not valid:
            print("Wrong way")
            return

        print("===================")
        print_map(snake_map)
        print("===================")
        print("\n")

        a_no_way = check_no_way_to_go(snake_map, 'A')
        if a_no_way:
            print("No way to go")
            return

        A_history = A_history + direction1

        sleep(0.5)
main()