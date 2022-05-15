# 부족한 금액 계산하기
# https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    total = (price + price * count) * count // 2
    return total - money if total > money else 0


print(solution(3, 20, 4))  # 10
