# 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862


def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    count = 0
    for num in sorted(lost_set):
        if num - 1 in reserve_set:
            reserve_set.remove(num - 1)
            count += 1
        elif num + 1 in reserve_set:
            reserve_set.remove(num + 1)
            count += 1
    return n - len(lost_set) + count


print(solution(5, [2, 4], [1, 3, 5]))  # 5
