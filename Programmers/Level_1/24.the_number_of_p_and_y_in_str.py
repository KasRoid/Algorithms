# 문자열 내 p 와 y 의 개수


def solution(s):
    return len([c for c in s.lower() if c == 'p']) == len([c for c in s.lower() if c == 'y'])


print(solution("pPoooyY"))
