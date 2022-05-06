# 하샤드 수

def solution(x):
    total = 0
    for c in str(x):
        total += int(c)
    return x % total == 0


print(solution(10))  # True
