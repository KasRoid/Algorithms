# [1차] 다트 게임
# https://programmers.co.kr/learn/courses/30/lessons/17682

import re

def solution(dartResult):
    match = re.match(r"([0-9]+[SDT][*#]?)([0-9]+[SDT][*#]?)([0-9]+[SDT][*#]?)", dartResult, re.I)
    items = match.groups()

    scores = []
    for i, item in enumerate(items):
        match = re.match(r"([0-9]+)([SDT])([*#]?)", item, re.I)
        info = match.groups()
        score = 0
        for c in info:
            if c.isdigit():
                score += int(c)
            elif c == 'D':
                score = score ** 2
            elif c == 'T':
                score = score ** 3
            elif c == '*':
                score *= 2
                if i > 0:
                    scores[i - 1] *= 2
            elif c == '#':
                score *= -1
        scores.append(score)
    return sum(scores)


print(solution('1S2D*3T'))  # 37
print(solution('1D2S#10S'))  # 9
print(solution('1D2S0T'))  # 3
print(solution('1S*2T*3S'))  # 23
print(solution('1D#2S*3S'))  # 5
print(solution('1T2D3D#'))  # -4
print(solution('1D2S3T*'))  # 59
