# 행렬의 곱셈
# https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    new_arr2 = []
    for i in range(len(arr2)):
        for k in range(len(arr2[i])):
            if len(new_arr2) < k + 1:
                new_arr2.append([arr2[i][k]])
            else:
                new_arr2[k].append(arr2[i][k])

    temp = []
    result = []
    for i in range(len(arr1)):
        for j in range(len(new_arr2)):
            for k in range(len(new_arr2[j])):
                num1 = arr1[i][k]
                num2 = new_arr2[j][k]
                temp.append(num1 * num2)
            if len(result) < i + 1:
                result.append([sum(temp)])
            else:
                result[i].append(sum(temp))
            temp.clear()
    return result


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))  # [[3, 3], [3, 3]]
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))  # [[22, 22, 11], [36, 28, 18], [29, 20, 14]]


# [[0, 0][0, 1]  [1, 0][1, 1]  [2, 0][2, 1]]

# [[0, 0][1, 0]  [0, 1][1, 1]]



def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [ [ 1, 2 ], [ 2, 3 ]]
b = [[ 3, 4], [5, 6]]
print("결과 : {}".format(productMatrix(a,b)));
