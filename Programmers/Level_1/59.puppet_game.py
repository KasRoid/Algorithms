# 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3


def solution(board, moves):
    answer = 0
    collection = []

    for move in moves:
        for i, line in enumerate(board):
            doll = line[move - 1]
            if doll:
                if [doll] == collection[-1:]:
                    collection.pop()
                    answer += 2
                else:
                    collection.append(doll)
                board[i][move - 1] = 0
                break
    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))  # 4
