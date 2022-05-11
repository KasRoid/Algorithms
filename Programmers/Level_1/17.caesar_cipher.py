# 시저 암호

# 공백은 아무리 밀어도 공백입니다.
# s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
# s의 길이는 8000이하입니다.
# n은 1 이상, 25이하인 자연수입니다.

def solution(s, n):
    answer = ''
    for c in s:
        if c.isupper():
            asc = ord(c) + n
            if asc > 90:
                r = asc % 90
                asc = 64 + r
            answer += chr(asc)
        elif c.islower():
            asc = ord(c) + n
            if asc > 122:
                r = asc % 122
                asc = 96 + r
            answer += chr(asc)
        else:
            answer += c
    return answer


print(solution("a B z", 4))
