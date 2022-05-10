# 이상한 문자열 만들기

# 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
# 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.


def solution(s):
    text = ""
    blank = ""
    arr = []
    for c in s:
        if c.isalpha():
            text += c
            if blank != "":
                arr.append(blank)
                blank = ""
        else:
            blank += c
            if text != "":
                arr.append(text)
                text = ""
    if text != "":
        arr.append(text)
    elif blank != "":
        arr.append(blank)

    return "".join(["".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(text)]) for text in arr])


print(solution("try hello world"))
