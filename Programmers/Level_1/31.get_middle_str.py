# 가운데 글자 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    mid = len(s) // 2
    return s[mid-1:mid+1] if len(s) % 2 == 0 else s[mid]

print(solution('abcde'))
