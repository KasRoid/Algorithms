# 최소 직사각형
# https://programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    # print(max(min(size) for size in sizes))
    print(max(sum(sizes, [])))
    print(max(sizes))
    print(sum(sizes, []))
    w = 0
    h = 0
    for size in sizes:
        w = max(w, min(size))
        h = max(h, max(size))
    return w * h


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))  # 4000
