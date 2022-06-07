# 최댓값과 최솟값
# https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    nums = [int(c) for c in s.split()]
    return " ".join([str(min(nums)), str(max(nums))])


print(solution("1 2 3 4"))  # "1 4"
print(solution("-1 -2 -3 -4"))  # "-4 -1"
print(solution("-1 -1"))  # "-1 -1"
