# 음양 더하기
# https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    return sum([num if signs[i] else -num for i, num in enumerate(absolutes)])


print(solution([4,7,12], [True,False,True]))  # 9
print(solution([1, 2, 3], [False,False,True]))  # 0
