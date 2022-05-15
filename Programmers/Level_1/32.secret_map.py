# 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    return [(bin(arr1[i] | arr2[i])).replace('0b', '').zfill(n).replace('1', '#').replace('0', ' ') for i in range(n)]


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))  # ["#####","# # #", "### #", "# ##", "#####"]
