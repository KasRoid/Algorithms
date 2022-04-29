# 리스트에서 가장 수익이 높은 구간을 찾아 합을 리턴하는 함수 구현

def sublist_max(profits):
    start_index = 0
    end_index = 0
    highest = 0
    new_value = 0
    for i in range(len(profits)):
        new_value = 0
        for j in range(len(profits[i:])):
            profit = profits[i + j]
            if highest == 0 & profit < 0:
                continue

            new_value += profit
            if highest < new_value:
                highest = new_value
                start_index = i
                end_index = i + j
    return sum(profits[start_index:end_index + 1])


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))
