# 줄 서는 방법
# https://programmers.co.kr/learn/courses/30/lessons/12936

def solution(n, k):
    result = []
    elements = [i for i in range(1, n + 1)]
    i = 0
    count = 0
    while len(elements) > 0:
        n -= 1
        while count + factorial(n) < k:
            count += factorial(n)
            i += 1
        result.append(elements[i])
        elements.pop(i)
        i = 0
    return result
    
    
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
    
    
print(solution(3, 5))  # [3,1,2]
