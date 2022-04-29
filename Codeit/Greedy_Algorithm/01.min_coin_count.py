# 최소 동전으로 돈을 거슬러 주는 Greedy Algorithm 함수 구현

def min_coin_count(value, coin_list):
    result = 0
    i = 0
    coins = sorted(coin_list, reverse=True)
    while value > 0:
        if value - coins[i] >= 0:
            value = value - coins[i]
            result += 1
        else:
            i += 1
    return result


# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))
