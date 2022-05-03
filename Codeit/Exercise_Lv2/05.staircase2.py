# 높이 n개의 계단을 올라가는 방법을 리턴한다
def staircase(stairs, possible_steps):
    cache = {}
    return calculate(stairs, possible_steps, cache)


def calculate(n, steps, cache):
    if n < 1:
        return 1

    if n >= steps[2]:
        cache[n] = calculate(n - steps[0], steps, cache) \
                   + calculate(n - steps[1], steps, cache) \
                   + calculate(n - steps[2], steps, cache)
    elif n >= steps[1]:
        cache[n] = calculate(n - steps[0], steps, cache) \
                   + calculate(n - steps[1], steps, cache)
    else:
        cache[n] = calculate(n - steps[0], steps, cache)
    return cache[n]


print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))
