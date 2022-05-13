# 두 정수 사이의 합

def solution(a, b):
    count = abs(a - b) + 1
    return int(count // 2 * (a + b) if count % 2 == 0 else count // 2 * (a + b) + (a + b) / 2)


print(solution(5, 3))
