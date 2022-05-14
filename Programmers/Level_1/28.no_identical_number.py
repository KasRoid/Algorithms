# 같은 숫자는 싫어

def solution(arr):
    result = []
    placeholder = None
    for n in arr:
        if placeholder != n:
            placeholder = n
            result.append(n)
    return result


print(solution([1,1,3,3,0,1,1]))
