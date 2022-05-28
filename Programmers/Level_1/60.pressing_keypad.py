# 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3

def solution(numbers, hand):
    answer = ''
    lh = -1
    rh = -2
    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [-1, 0, -2]
    ]
    key_loc = {}

    for i, line in enumerate(keypad):
        for j, digit in enumerate(line):
            key_loc[digit] = [i, j]

    for number in numbers:
        if number in set([1, 4, 7]):
            answer += 'L'
        elif number in set([3, 6, 9]):
            answer += 'R'
        else:
            l_move = abs(key_loc[number][0] - key_loc[lh][0]) + abs(key_loc[number][1] - key_loc[lh][1])
            r_move = abs(key_loc[number][0] - key_loc[rh][0]) + abs(key_loc[number][1] - key_loc[rh][1])
            if l_move > r_move:
                answer += 'R'
            elif r_move > l_move:
                answer += 'L'
            else:
                answer += 'R' if hand == 'right' else 'L'

        if answer[-1] == 'R':
            rh = number
        else:
            lh = number
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))  # "LRLLLRLLRRL"
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))  # "LRLLRRLLLRR"
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))  # "LLRLLRLLRL"
