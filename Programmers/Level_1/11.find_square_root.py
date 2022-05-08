# 정수 제곱근 판별

from math import sqrt


def solution(n):
    return int((sqrt(n) + 1) ** 2) if sqrt(n).is_integer() else -1


# Solving without math module
def solution(n):
    return int((n ** 0.5 + 1) ** 2) if n ** 0.5 % 1 == 0 else -1


print(solution(121))
