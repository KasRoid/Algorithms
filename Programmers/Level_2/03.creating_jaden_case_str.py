# JadenCase 문자열 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    words = []
    word = ""
    space = ""
    for c in s:
        if c.isalpha() or c.isdigit():
            if len(space):
                words.append(space)
                space = ""
            word += c
        else:
            if len(word):
                words.append(word)
                word = ""
            space += c
    if len(word):
        words.append(word)
    if len(space):
        words.append(space)
    return "".join(w.lower().capitalize() for w in words)


print(solution("3people unFollowed me"))  # "3people Unfollowed Me"
