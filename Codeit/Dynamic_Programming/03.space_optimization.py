# 공간복잡도를 최소화하여 피보나치 수를 계산하는 함수 구현.

def fib_optimized(n):
    current = 1
    previous = 1

    for i in range(1, n + 1):
        if i <= 2:
            continue
        previous, current = current, previous + current
    return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
