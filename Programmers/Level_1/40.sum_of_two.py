# 두 개 뽑아서 더하기
# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    result = sorted(list({num1 + num2 for j, num2 in enumerate(numbers) for i, num1 in enumerate(numbers) if i != j}))
    return result


print(solution([2,1,3,4,1]))  # [2,3,4,5,6,7]
