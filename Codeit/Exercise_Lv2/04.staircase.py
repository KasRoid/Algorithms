# 계단을 한 칸 혹은 두 칸씩 올라가는 방법이 총 몇 개인지 구하는 함수 구현

def staircase(n):
    cache = {}
    return calculate(n, cache)


def calculate(n, cache):
    if n < 2:
        return 1
    if n in cache:
        return cache[n]
    result = calculate(n - 1, cache) + calculate(n - 2, cache)
    cache[n] = result
    return result


# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
