def select_stops(water_stops, capacity):
    result = []
    current = 0
    placeholder = 0
    should_end = False

    while not should_end:
        for i, stop in enumerate(water_stops):
            if i == len(water_stops) - 1:
                if not water_stops[placeholder] in result:
                    result.append(water_stops[placeholder])
                result.append(stop)
                should_end = True
                break
            if stop - current <= capacity:
                placeholder = i
            else:
                result.append(water_stops[placeholder])
                current = water_stops[placeholder]
                water_stops = water_stops[placeholder + 1:]
                break
    return result


# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))
