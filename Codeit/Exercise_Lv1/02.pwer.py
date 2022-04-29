# 거듭 제곱을 계산하는 함수를 시간복잡도 O(lg y) 로 구현

def power(x, y):
    if y == 1:
        return x
    else:
        if y % 2 == 0:
            b = y // 2
        else:
            b = y // 2 + 1
        a = y // 2
    return power(x, a) * power(x, b)


# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))
