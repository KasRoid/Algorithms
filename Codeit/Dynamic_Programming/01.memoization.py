# n번째 피보나치 수를 찾아 주는 함수를 Memoization 기법을 사용해 구현.

def fib_memo(n, cache):
    if n < 3:
        return 1
    if n in cache:
        return cache[n]
    else:
        cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
        return cache[n]


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))
