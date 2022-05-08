# 최대공약수와 최소공배수
# 유클리드 호제법으로 풀어야 간단하다.

def solution(n, m):
    mul = n * m
    while n % m != 0:
        n, m = m, n % m
    return [m, int(mul / m)]


print(solution(4, 12))
