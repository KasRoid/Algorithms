# 파라미터로 정수값 n을 받고 n의 각 자릿수의 합을 리턴해주는 재귀함수 sum_digits를 쓰세요.

# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    str_n = str(n)
    if len(str_n) < 2:
        return n
    return int(str_n[0]) + sum_digits(int(str_n[1:]))


# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))
