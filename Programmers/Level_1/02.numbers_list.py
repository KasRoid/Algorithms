# x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = []
    number = x
    for _ in range(n):
        answer.append(number)
        number += x
    return answer


print(solution(2, 5))  # [2,4,6,8,10]
