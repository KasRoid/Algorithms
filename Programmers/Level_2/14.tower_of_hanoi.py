# 하노이의 탑
# https://programmers.co.kr/learn/courses/30/lessons/12946

def solution(n):
    answer = []
    hanoi(n, 1, 3, answer)
    return answer


def hanoi(n, start, end, answer):
    if n == 0:
        return
    vacant = 6 - start - end
    hanoi(n - 1, start, vacant, answer)
    answer.append([start, end])
    hanoi(n - 1, vacant, end, answer)


print(solution(2))  # [ [1,2], [1,3], [2,3] ]
