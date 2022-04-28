# 가능한 최대 수익을 반환하는 함수를 Tabulation 방식으로 구현
# price_list: 개수별 가격이 정리된 있는 리스트
# count: 판매할 갯수

def max_profit(price_list, count):
    table = [price_list[0], price_list[1]]
    result = 0

    i = 2
    while i <= count:
        if i < len(price_list):
            result = price_list[i]
        for index in range(1, i // 2 + 1):
            result = max(result, table[index] + table[i - index])
        table.append(result)
        print(table)
        i += 1
    return table[count]


# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
