# 문자열 내림차순으로 배치하기

def solution(s):
    answer = list(s)
    answer.sort(reverse=True)
    return "".join(answer)


print(solution("Zbcdefg"))
