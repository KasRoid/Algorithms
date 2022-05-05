def sum_in_list(search_sum, sorted_list):
    isPresent = False
    for number in sorted_list:
        key = search_sum - number
        isPresent = binary_search(key, sorted_list)
        if isPresent:
            return True
    return False


def binary_search(key, sorted_list) -> bool:
    if len(sorted_list) == 0:
        return False
    mid = len(sorted_list) // 2
    if key == sorted_list[mid]:
        return True
    elif key < sorted_list[mid]:
        return binary_search(key, sorted_list[:mid])
    else:
        return binary_search(key, sorted_list[mid + 1:])


print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))
