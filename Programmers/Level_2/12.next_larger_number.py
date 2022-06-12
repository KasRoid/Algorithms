# 다음 큰 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12911


def solution(n):
    base = (bin(n)[2:]).count('1')
    new_base = None
    while base != new_base:
        n += 1
        new_base = (bin(n)[2:]).count('1')
    return n


print(solution(78))  # 83
print(solution(15))  # 23
