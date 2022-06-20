# 숫자 블록
# https://programmers.co.kr/learn/courses/30/lessons/12923

def solution(begin, end):
    return [0 if num == 1 else divisor(num) for num in range(begin, end + 1)]


def divisor(num):
    result = 1
    for divider in range(2, int(num ** 0.5) + 1):
        if num // divider > 10 ** 7:
            continue
        if num % divider == 0:
            result = int(num / divider)
            break
    return result


print(solution(1, 10))  # [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]
