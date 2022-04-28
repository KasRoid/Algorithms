# n번째 피보나치 수를 찾아주는 함수를 tabulation 기법을 사용해 구현

def fib_tab(n):
    cache = {}
    for i in range(1, n + 1):
        if i <= 2:
            cache[i] = 1
            continue
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[n]


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))
