# 멀리 뛰기
# https://programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    if n == 1:
        return 1
    cache = [1, 2]
    while len(cache) < n:
        cache.append(cache[-1] + cache[-2])
    return cache.pop() % 1234567


print(solution(4))  # 5
print(solution(3))  # 3
