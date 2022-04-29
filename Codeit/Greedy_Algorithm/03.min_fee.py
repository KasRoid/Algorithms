# 리스트에 있는 숫자만큼의 프린트물을 출력해야 한다.
# 프린터는 1개뿐이라 뒷 순서는 앞 순서 끝날 때까지 기다려야 한다.
# 모든 사람의 대기시간 합이 가장 짧은 경우를 Greedy Algorithm 으로 구현

def min_fee(pages_to_print):
    result = 0
    for index, time in enumerate(sorted(pages_to_print)):
        result += time * (len(pages_to_print) - index)
        print(f'Time: {time}, People: {len(pages_to_print) - index}, Result: {result}')
    return result


# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
