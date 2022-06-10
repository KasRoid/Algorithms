# k진수에서 소수 개수 구하기
# https://programmers.co.kr/learn/courses/30/lessons/92335

def solution(n, k):
    num = convert(n, k)
    candidates = list(filter(lambda x: x.isdigit(), num.split('0')))
    return len(list(filter(isPrime, map(int, candidates))))

def convert(n, k):
    answer = []
    while n >= k:
        answer.append(n % k)
        n //= k
    answer.append(n)
    return "".join(reversed(list(map(str, answer))))

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print(solution(437674, 3))  # 3
print(solution(110011, 10))  # 2
