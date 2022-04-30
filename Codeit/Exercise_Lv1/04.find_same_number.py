# 주어진 리스트에서 중복되는 어떠한 수 '하나' 를 반환하는 함수 구현
# 리스트 내 중복되는 수가 여러개이더라도 하나만 반환하면 된다.

def find_same_number(some_list):
    for i, number in enumerate(some_list):
        for another_number in some_list[i + 1:]:
            if number == another_number:
                return number


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
