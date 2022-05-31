# 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484


def solution(lottos, win_nums):
    lottos_set = set(lottos)
    minimum = len(lottos_set - (lottos_set - set(win_nums)))
    if 0 in lottos_set:
        lottos_set.remove(0)
    maximum = 6 - (len(lottos_set)) + minimum
    return [min(6, 7 - maximum), min(6, 7 - minimum)]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))  # [3, 5]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))  # [1, 1]
