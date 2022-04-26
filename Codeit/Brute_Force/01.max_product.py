# 카드 두 뭉치가 있다.
# 왼쪽 뭉치에서 카드를 하나 뽑고 오른쪽 뭉치에서 카드를 하나 뽑아서, 두 수의 곱이 가장 크게 나오는 경우를 찾으시오.


def max_product(left_cards, right_cards):
    result = 0
    for left_card in left_cards:
        for right_card in right_cards:
            if result < left_card * right_card:
                result = left_card * right_card
    return result


# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))
