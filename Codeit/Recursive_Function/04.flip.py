# 파라미터로 리스트 some_list를 받고, 뒤집힌 리스트를 리턴해 주는 재귀 함수 flip을 쓰세요.

# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    if len(some_list) < 2:
        return some_list
    last_index = len(some_list) - 1
    return [some_list[last_index]] + flip(some_list[:last_index])


# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)