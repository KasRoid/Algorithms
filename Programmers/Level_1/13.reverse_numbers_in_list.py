# 자연수 뒤집어 배열로 만들기

def solution(n):
    return list(reversed([int(i) for i in str(n)]))


print(solution(2356780))
