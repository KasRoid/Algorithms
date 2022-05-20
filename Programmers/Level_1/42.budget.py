# 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    total = 0
    for i, money in enumerate(sorted(d)):
        total += money
        if total > budget:
            return i
    return len(d)


print(solution([1,3,2,5,4], 9))  # 3
