# N-Queen
# https://programmers.co.kr/learn/courses/30/lessons/12952

def solution(n):
    count = [0]
    for loc in range(n):
        queens = []
        dfs(queens, loc, count, n)
    return count[0]


def dfs(queens, loc, count, n):
    if loc in queens:
        return
    for r, c in enumerate(queens):
        h = len(queens) - r
        if loc == c - h or loc == c + h:
            return
    queens.append(loc)
    if len(queens) == n:
        count[0] += 1
        return
    for loc in range(n):
        dfs(queens.copy(), loc, count, n)


print(solution(4))  # 2
