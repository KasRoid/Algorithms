# 문자열 다루기 기본

def solution(s):
    if not len(s) == 4 or len(s) == 6:
        return False

    try:
        int(s)
    except ValueError:
        return False
    return True

print(solution("a1234"))
