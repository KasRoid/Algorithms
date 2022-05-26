# 소수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12977

def solution(nums):
    result = 0
    nums = list(set(nums))
    cases = {}
    max_value = 0

    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                sum_value =  nums[i] + nums[j] + nums[k]
                max_value = max(max_value, sum_value)
                cases[sum_value] = cases[sum_value] + 1 if sum_value in cases else 1
    
    primes = {num for num in range(2, max_value + 1)}
    for num in range(2, max_value + 1):
        if num in primes:
            primes -= set(range(num * 2, max_value + 1, num))

    for key, value in cases.items():
        if key in primes:
            result += value
    return result


print(solution([1,2,3,4]))  # 1
print(solution([1,2,7,6,4]))  # 4
