# 이진 탐색 알고리즘을 재귀적으로 구현하기

def binary_search(element, some_list, start_index=0, end_index=None):

    if end_index is None:
        end_index = len(some_list) - 1  # 4
    midpoint = (start_index + end_index) // 2  # 2, 1

    if element == some_list[midpoint]:
        return midpoint
    elif element > some_list[midpoint]:
        start_index = midpoint + 1
    elif element < some_list[midpoint]:
        end_index = midpoint

    if start_index == end_index:
        if some_list[start_index] == element:
            return start_index
        else:
            return None
    return binary_search(element, some_list, start_index, end_index)


# 테스트
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
