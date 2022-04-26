# 배열 안의 숫자는 댐의 높이이다. 각 댐 사이에 물을 채울 경우 얼마까지 채울 수 있을까?
# 높이가 3인 댐이 있고 빈 공간을 하나 건너 높이 4인 댐이 있다면 물이 흘러내리지 않게 채울 수 있는 양은 3이다.

def trapping_rain(buildings):
    width = 0
    left = 0
    obstacle = 0
    result = 0
    current_index = 0

    for i in range(len(buildings)):
        if i < current_index:
            continue

        building = buildings[i]
        if left == 0 and building == 0:
            continue
        if left == 0 and building != 0:
            left = building

        for j in range(i + 1, len(buildings)):
            right = buildings[j]

            if left <= right:
                result += width * min(left, right) - obstacle
                width = 0
                obstacle = 0
                left = right
                current_index = j
                break
            else:
                width += 1
                obstacle += right
                if j == len(buildings) - 1:
                    width = 0
                    obstacle = 0
                    left = 0
    return result


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

# 정답
# 10
# 6
