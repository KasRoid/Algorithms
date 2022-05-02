# 파라미터로 일별 주식 가격을 받고 최대 수익을 리턴하는 함수 구현
# 주식은 단 한번만 사고 팔며, 구매 당일에는 판매할 수 없음

def max_profit(stock_list):
    profits = []
    prev_value = 0
    for index, stock in enumerate(stock_list):
        if index == 0:
            prev_value = stock
            profits.append(0)
        else:
            profit = stock - prev_value
            prev_value = stock
            profits.append(profit)

    current = profits[1]
    max_value = profits[1]
    for profit in profits[2:]:
        current = max(current + profit, profit)
        max_value = max(max_value, current)
    return max_value


# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))
