# 피보나치 수
# https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    cache = [0, 1, 1]
    while len(cache) <= n:
        cache.append(cache[-1] + cache[-2])
    return cache.pop() % 1234567


print(solution(3))  # 2
print(solution(5))  # 5
