# -'- coding: utf-8 -*-
import sys
import json
from random import choice


def create_map_find_location(map_string, player, opp):
    map_str = [['0']*12, ['0']*12]
    for i in range(8):
        map_str.append(['0']*2 + list(map_string[8*i:8*i+8].replace('*', '1').replace(opp, '0').replace('a', '0').replace('b', '0')) + ['0']*2)
        if player in map_str[i+2]:
            r = i + 2
            c = map_str[i+2].index(player)
    map_str.extend([['0']*12, ['0']*12])
    return map_str, (r, c)


def check_available(map_str, r, c):
    ava_dict = {'U': 0, 'D': 0, 'L': 0, 'R': 0}
    ava_dict['U'] = sum([ int(map_str[r-2][c]), int(map_str[r-1][c])*2 ]) if int(map_str[r-1][c]) != 0 else 0
    ava_dict['D'] = sum([ int(map_str[r+2][c]), int(map_str[r+1][c])*2 ]) if int(map_str[r+1][c]) != 0 else 0
    ava_dict['R'] = sum([ int(map_str[r][c+2]), int(map_str[r][c+1])*2 ]) if int(map_str[r][c+1]) != 0 else 0
    ava_dict['L'] = sum([ int(map_str[r][c-2]), int(map_str[r][c-1])*2 ]) if int(map_str[r][c-1]) != 0 else 0
    return ava_dict


def cal_score(map_str, r, c):
    ava_dict = check_available(map_str, r, c)
    area_score = {'UR': 0, 'UL': 0, 'DR': 0, 'DL': 0}
    coor_dict = {'U': (-2, 0), 'D': (0, +2), 'L': (-2, 0), 'R': (+1, +3)}
    mask_dict = {'UR': [2, 1, 3, 2], 'UL': [1, 2, 2, 3], 'DR': [3, 2, 2, 1], 'DL': [2, 3, 1, 2]}
    flatten = lambda lst: [y for x in lst for y in x]
    cal = lambda x_li, y_li: sum(x*y for x, y in zip(x_li, y_li))
    for k in area_score.keys():
        r1, r2 = coor_dict[k[0]]
        c1, c2 = coor_dict[k[1]]
        area_score[k] = cal(flatten([list(map(int, x[(c+c1):(c+c2)])) for x in map_str[(r+r1):(r+r2)]]), mask_dict[k]) + ava_dict[k[0]] + ava_dict[k[1]]
    return area_score


def first_move(score_area, result, not_ava_move):
    # for k, v in score_area.items():
    #     if v > result['max_score']:
    #         result['max_score'] = v
    #         result['move'] = k
    # for k, v in score_area.items():
    #     if (v > 0) & (k != result['move']) & (''.join(not_ava_move) != k):
    #         result['candidate'].append(k)
    for k, v in score_area.items():
        if v > result['max_score']:
            result['max_score'] = v
            result['move'] = k
    for k, v in score_area.items():
        if len(not_ava_move) <= 2:
            if (v > 0) & (k != result['move']) & (''.join(not_ava_move) != k):
                result['candidate'].append(k)
    if len(result['candidate']) == 0:
        result['candidate'].append(0)
    return result


def second_move(result, ava_move, score_area):
    if len(result['candidate']) == 1:
        return ava_move[0]
    elif len(result['candidate']) == 2:
        c1, c2 = result['candidate']
        if score_area[c1] == score_area[c2]:
            return choice(ava_move)
        elif score_area[c1] > score_area[c2]:
            return [x for x in c1 if x in ava_move][0]
        else:
            return [x for x in c2 if x in ava_move][0]
    else:
        choose_min = sorted([(c, score_area[c]) for c in result['candidate']], key=lambda x: x[1])[0][0]
        return [x for x in choose_min if x in ava_move][0]


def move(map_str, r, c):
    ava_dict = check_available(map_str, r, c)
    not_ava_move = [k for k, v in ava_dict.items() if v <= 0]
    ava_move = [k for k, v in ava_dict.items() if v > 0]

    score_area = cal_score(map_str, r, c)
    result = {'move': None, 'max_score': 0, 'candidate': []}
    # first move
    result = first_move(score_area, result, not_ava_move)

    # second move

    r = second_move(result, ava_move, score_area)
    return r


def main():
    """
    인풋은 json형식으로 들어오며
    'map' : 8 * 8 크기의 판의 상태를 한 칸당 한 글자로 공백없이 string의 형태로 준다.
    'opponent_history' : 지금까지 상대가 움직인 방향들을 string의 형태로 공백없이 준다. ex) 'UDDLLUR'
    'my_history' : 지금까지 내가 움직인 방향들을 string의 형태로 공백없이 준다.        ex) 위와 동일
    'me' : 내가 누군지 알려줌.          ex) 'A' or 'B'
    'opponent' : 상대가 누군지 알려줌.  ex) 위와 동일

    map에 대한 상세한 설명
    💎 : 갈 수 있는 곳입니다. 젬이라고 불리죠
    A, B : 위에서 설명했듯 인풋중 me로 들어온 알파벳이 본인이 움직일 말이 됩니다.
    a, b : A, B가 이미 지나간 길, 다시 말해 다시는 갈 수 없는 길입니다.
    """

    data = json.loads(sys.argv[1])

    map_string = data['map']
    opponent_history = data['opponent_history']
    my_history = data['my_history']
    player = data['me']
    opponent = data['opponent']

    map_str, (r, c) = create_map_find_location(map_string=map_string, player=player, opp=opponent)
    print(move(map_str, r, c))


main()