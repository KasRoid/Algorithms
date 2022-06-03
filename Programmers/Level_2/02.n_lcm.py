# n개의 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):
    if len(arr) == 1:
        return arr[0]
    num1 = arr.pop()
    num2 = arr.pop()
    dividend = max(num1, num2)
    divisor = min(num1, num2)
    while divisor > 0:
        divisor, dividend = dividend % divisor, divisor
    arr.append(num1 * num2 / dividend)
    return solution(arr)


print([2,6,8,14])  # 168
print([1,2,3])  # 6
