# 정렬된 두 리스트를 받아서 하나의 정렬된 리스트를 반환하는 합병 정렬 알고리즘 구현

def merge(list1, list2):
    result = []
    is_empty = False
    while not is_empty:
        if not list1 and not list2:
            is_empty = True
        elif not list1:
            result.append(list2.pop(0))
        elif not list2:
            result.append(list1.pop(0))
        elif list1[0] < list2[0]:
            result.append(list1.pop(0))
        elif list1[0] > list2[0]:
            result.append(list2.pop(0))
    return result


# 테스트
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))
