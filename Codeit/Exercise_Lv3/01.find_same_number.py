# 전달받은 리스트에서 반복되는 요소를 찾는 함수 구현

def find_same_number(some_list, start=1, end=None):
    if end is None:
        end = len(some_list) - 1

    if start == end:
        return end

    mid = (start + end) // 2 + 1
    below_half = 0
    for number in some_list:
        if start <= number < mid:
            below_half += 1

    if below_half > mid - start:
        return find_same_number(some_list, start, mid - 1)
    else:
        return find_same_number(some_list, mid, end)


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
