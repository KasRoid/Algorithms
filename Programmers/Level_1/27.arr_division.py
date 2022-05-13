# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = sorted([n for n in arr if n % divisor == 0])
    return answer if len(answer) != 0 else [-1]


print(solution([5, 9, 7, 10], 5))
print(solution([3,2,6], 10))
