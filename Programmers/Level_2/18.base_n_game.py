# n진수 게임
# https://programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    result = ""
    converted = []
    count = 0
    while len(converted) < t * m:
        for c in convert(count, n):
            converted.append(c)
        count += 1
    p = p - 1
    for i in range(t):
        result += converted[p + i * m]
    return result


def convert(num, base):
    converted = ""
    while num != 0:
        converted += str(num % base) if num % base < 10 else chr(65 + num % base % 10)
        num = num // base
    return converted[::-1] if converted else "0"
