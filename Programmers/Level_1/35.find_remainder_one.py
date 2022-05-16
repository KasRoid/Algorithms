# 나머지가 1이 되는 수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    primes = set(range(2, n + 1))
    for i in range(2, n + 1):
        if i in primes:
            if n % i == 1:
                return i
            primes -= set(range(i * 2, n + 1, i))
        
        
print(solution(12))  # 11
