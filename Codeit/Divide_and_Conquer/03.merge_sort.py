# Divide and Conquer 방식으로 Merge Sort 구현
# 리스트를 받아 리스트를 반환한다.

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


# 합병 정렬
def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list

    mid_index = len(my_list) // 2
    list1 = my_list[:mid_index]
    list2 = my_list[mid_index:]
    return merge(merge_sort(list1), merge_sort(list2))


# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
