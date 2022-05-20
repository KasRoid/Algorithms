# 약수의 개수와 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/77884


def solution(left, right):
    return sum([num if num % (num ** 0.5) else -num for num in range(left, right + 1)])

print(solution(13, 17))  # 43
print(solution(24, 27))  # 52
