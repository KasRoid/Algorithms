# 문자열 내 마음대로 정렬하기

def solution(strings, n):
    return divide(strings, n)

def divide(strings, n):
    count = len(strings)
    if count == 1:
        return strings
    mid = count // 2
    left = strings[:mid]
    right = strings[mid:]
    return merge(divide(left, n), divide(right, n), n)

def merge(left, right, n):
    result = []
    i = n
    while len(left) != 0 and len(right) != 0:
        l_element = left[0]
        r_element = right[0]
        if l_element[i] < r_element[i]:
            result.append(left.pop(0))
            i = n
        elif l_element[i] > r_element[i]:
            result.append(right.pop(0))
            i = n
        else:
            result.append(left.pop(0) if l_element < r_element else right.pop(0))
            
    return result + right if len(left) == 0 else result + left

print(solution(["abce", "abcd", "cdx"], 1))
