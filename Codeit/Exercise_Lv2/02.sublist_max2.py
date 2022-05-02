def sublist_max(profits):
    total = 0
    max_total = 0
    for profit in profits:
        if total + profit > 0:
            total += profit
            max_total = max(max_total, total)
        else:
            total = 0
    return max_total


# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))
