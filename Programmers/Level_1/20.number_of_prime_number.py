# 소수 찾기

def solution(n):
    return len([i for i in range(2, n + 1) if is_prime(i)])


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False

    r = int(n ** 0.5)
    f = 5

    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


# 에라토스테네스의 체
def solution(n):
    num = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    return len(num)

print(solution(10000000))
