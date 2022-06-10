# 숫자의 표현
# https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    if n == 1 or n == 2:
        return 1
    counter = 1
    mid = n // 2 + 2
    for i in range(1, mid):
        total = 0
        for j in range(i, mid):
            total += j
            if total > n:
                break
            elif total == n:
                counter += 1
                break
    return counter


print(solution(2))  # 4


def expressions(num):
    return len([i for i in range(1, num + 1, 2) if num % i is 0])
