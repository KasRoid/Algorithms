# 1부터 n까지 더하는 함수 구현

def consecutive_sum(start, end):
    if start == end:
        return end
    return start + consecutive_sum(start + 1, end)


# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))
