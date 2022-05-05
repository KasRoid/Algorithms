def trapping_rain(buildings):
    total = 0
    left_list = [buildings[0]]
    right_list = [buildings[-1]]

    for building in buildings[1:]:
        left_list.append(max(building, left_list[-1]))

    for building in reversed(buildings[:-1]):
        right_list.append(max(building, right_list[-1]))
    right_list.reverse()

    for i, building in enumerate(buildings):
        total += min(left_list[i], right_list[i]) - building

    return total


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
