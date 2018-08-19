# -'- coding: utf-8 -*-
# codes from https://gist.github.com/steve806/dbb104ba3070cc23972ecca28745074b
import sys
import json
from random import choice

import math


def dotproduct(v1, v2):
    return sum((a * b) for a, b in zip(v1, v2))


def length(v):
    return math.sqrt(dotproduct(v, v))


def angle(v1, v2):
    return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))


def get_position_from_location(location):
    return location[1] + location[0] * 8


def get_location_from_position(position):
    return (position % 8, position // 8)


def get_player_location(map_yx, player):
    for y in range(0, 8):
        for x in range(0, 8):
            if map_yx[y][x] == player:
                return (y, x)
    return (-1, -1)


def tuple_sum(a, b):
    return (a[0] + b[0], a[1] + b[1])


def next_step(step):
    if step == 'U':
        return (-1, 0)
    elif step == 'D':
        return (1, 0)
    elif step == 'L':
        return (0, -1)
    elif step == 'R':
        return (0, 1)
    return (0, 0)


def is_available(map_yx, location):
    position = get_position_from_location(location)
    if position < 0 or (location[0] < 0 or location[0] >= 8 or location[1] < 0 or location[1] >= 8):
        return False

    ret = map_yx[location[0]][location[1]]
    if ret != '*':
        return False
    return True


is_debug = False


def main():
    '''
        아래는 처음 판의 상태이다.
        위로 가고 싶을 경우 U, 아래로 가고 싶을 경우 D,
        오른쪽으로 가고 싶을 경우 R, 왼쪽으로 가고 싶을 경우 L
        을 출력해주면 된다.
        인풋은 json형식으로 들어오며
        'map' : 8 * 8 크기의 판의 상태를 한 칸당 한 글자로 공백없이 string의 형태로 준다.
        'opponent_history' : 지금까지 상대가 움직인 방향들을 string의 형태로 공백없이 준다. ex) 'UDDLLUR'
        'my_history' : 지금까지 내가 움직인 방향들을 string의 형태로 공백없이 준다.        ex) 위와 동일
        'me' : 내가 누군지 알려줌.          ex) 'A' or 'B'
        'opponent' : 상대가 누군지 알려줌.  ex) 위와 동일

        map에 대한 상세한 설명
        💎 : 갈 수 있는 곳입니다. 젬이라고 불리죠
        A, B : 위에서 설명했듯 me로 들어온 알파벳이 본인이 움직일 말이 됩니다.
        a, b : A, B가 이미 지나간 길, 다시말해 다시는 갈 수 없는 길입니다.
    '''

    ########################
    #                      #
    #  A 💎💎💎💎💎💎💎  #
    #  💎💎💎💎💎💎💎💎  #
    #  💎💎💎💎💎💎💎💎  #
    #  💎💎💎💎💎💎💎💎  #
    #  💎💎💎💎💎💎💎💎  #
    #  💎💎💎💎💎💎💎💎  #
    #  💎💎💎💎💎💎💎💎  #
    #  💎💎💎💎💎💎💎B   #
    #                      #
    ########################

    if (is_debug):
        data = json.loads(argv[2])
    else:
        data = json.loads(sys.argv[1])
    map_string = data['map']
    opponent_history = data['opponent_history']
    my_history = data['my_history']
    player = data['me']
    opponent = data['opponent']

    # 재미를 위해 젬을 직접 이용해서 코드를 짜보세요!
    new_input_str = map_string.replace("*", "💎")

    map_yx = []

    for i in range(8):
        map_yx.append(list(map_string[8 * i:8 * i + 8]))

    # TODO: 아래쪽을 변경하여 멋진 코드를 만들어 주세요!
    available = [['U', (0, -1), 0], ['D', (0, 1), 0], ['R', (1, 0), 0], ['L', (-1, 0), 0]]
    location = get_player_location(map_yx, player)
    position = get_position_from_location(location)

    # check availables
    for i in range(0, len(available)):
        if is_available(map_yx, tuple_sum(location, next_step(available[i][0]))):
            available[i][2] = 1.0

    available_target = sorted([x for x in available], key=lambda x: x[2], reverse=True)
    # calc opponent's center
    if opponent_history:
        op_x = 0
        op_y = 0
        for j in range(8):
            for i in range(8):
                if 'b' == map_yx[j][i]:
                    op_x += i;
                    op_y += j
        op_x /= len(opponent_history)
        op_y /= len(opponent_history)
        for i in range(len(available_target)):
            if available_target[i][2] == 0:
                continue
            a = angle(available_target[i][1], (op_x, op_y))
            if a == 0.0:
                a = math.inf
            else:
                a = a
            available_target[i][2] = a
        available_target = sorted([x for x in available], key=lambda x: x[2], reverse=True)
        # print(available_target)

    ret = available_target[0][0]
    if (is_debug):
        return bytes(ret, 'utf-8')
    else:
        print(ret)


if is_debug == False:
    main()