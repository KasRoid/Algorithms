# 올바른 괄호
# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    count = 0
    for c in s:
        count = count + (1 if c == '(' else -1)
        if count < 0:
            return False
    return count == 0
    