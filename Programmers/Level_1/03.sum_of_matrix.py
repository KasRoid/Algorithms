# 행렬의 덧셈

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            if len(answer) == i + 1:
                answer[i].append(arr1[i][j] + arr2[i][j])
            else:
                answer.append([arr1[i][j] + arr2[i][j]])
    return answer


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))  # [[4, 6], [7, 9]]
