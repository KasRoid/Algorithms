# 직선거리가 가장 가까운 두 매장을 찾아라.
from math import sqrt


# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)


# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):

    min_index1 = 0
    min_index2 = 0
    min_distance = 0

    for index1 in range(len(coordinates)):
        for index2 in range(len(coordinates)):
            if index1 == index2:
                continue
            store1 = coordinates[index1]
            store2 = coordinates[index2]
            if min_distance == 0:
                min_distance = distance(store1, store2)
            elif min_distance > distance(store1, store2):
                min_distance = distance(store1, store2)
                min_index1 = index1
                min_index2 = index2
    return [coordinates[min_index1], coordinates[min_index2]]


# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))
