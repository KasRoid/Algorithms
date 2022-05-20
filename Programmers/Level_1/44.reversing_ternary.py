# 3진법 뒤집기
# https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    digits = []
    while n != 0:
        remainder = n % 3
        digits.append(remainder)
        quotient = n // 3
        if n // 3 < 3 and quotient != 0:
            digits.append(quotient)
            break
        n = quotient
    print(digits)
    return sum([3 ** (len(digits) - 1 - i) * digit for i, digit in enumerate(digits)])


print(solution(2))  # 7
print(solution(45))  # 7
print(solution(125))  # 229
