# Quick Sort 구현
# quicksort 함수는 정렬된 새로운 리스트를 리턴하는 게 아니라, 파라미터로 받는 리스트 자체를 정렬시켜야 한다.

# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    return my_list


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    p = my_list[end]
    b = start
    for index in range(len(my_list[start:end])):
        if my_list[start + index] < p and b < start + index:
            swap_elements(my_list, b, start + index)
            b += 1
        elif my_list[start + index] < p:
            b += 1
    swap_elements(my_list, b, end)
    return b


def quicksort(my_list, start, end):
    if end - start < 1:
        return
    p = partition(my_list, start, end)
    quicksort(my_list, start, p - 1)
    quicksort(my_list, p + 1, end)


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)
