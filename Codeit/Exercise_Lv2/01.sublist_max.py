# 리스트에서 가장 수익이 높은 구간을 찾아 합을 리턴하는 함수 구현
# Divide and Conquer 방식으로 구현

def sublist_max(profits, start, end):
    if start == end:
        return profits[start]
    p = len(profits) // 2

    left_max = 0
    right_max = 0
    mid_max = 0
    return max(left_max, right_max, mid_max)


def max_crossing_sum(profits, start, end):
    p = len(profits) // 2
    if p == start | p == end:
        return


# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))
