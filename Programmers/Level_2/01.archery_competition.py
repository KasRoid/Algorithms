# 양궁대회
# https://programmers.co.kr/learn/courses/30/lessons/92342

def solution(n, info):
    max_score_diff = 0
    score_list = [(0, [0] * 11)]
    result = []
    
    while score_list:
        data = score_list.pop()
        idx, scores = data
        
        if idx < 10 and sum(scores) < n:
            score_copy = scores.copy()
            score_list.append((idx + 1, score_copy))
            new_scores = scores.copy()
            new_scores[idx] = info[idx] + 1
            score_list.append((idx + 1, new_scores))
        elif idx == 10 or sum(scores) == n:
            if sum(scores) < n:
                scores[-1] = n - sum(scores)
            if sum(scores) > n:
                continue
            ryan = 0
            apeach = 0
            for i in range(len(scores)):
                if scores[i] > info[i]:
                    ryan += 10 - i
                elif info[i]:
                    apeach += 10 - i
            diff = ryan - apeach
            if diff >= max_score_diff:
                if diff > max_score_diff:
                    max_score_diff = diff
                    result.clear()
                result.append(scores)
    if result:
        smallest_index = float('inf')
        smallest_score = None
        for scores in result:
            for i in range(len(scores)):
                if list(reversed(scores))[i]:
                    if i < smallest_index:
                        smallest_index = i
                        smallest_score = scores
        if smallest_score and max_score_diff:
            return smallest_score
    return [-1]


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))  # [0,2,2,0,1,0,0,0,0,0,0]
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))  # [-1]
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))  # [1,1,2,0,1,2,2,0,0,0,0]
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))  # [1,1,1,1,1,1,1,1,0,0,2]


# 발당 평균점수를 구하는 방식으로 접근했지만 실패

# def solution(n, info):
#     average = [(10 - i) * 2 / (a + 1) if a > 0 else 10 - i for i, a in enumerate(info)]
#     scores = sorted([(10 - i, a) for i, a in enumerate(average)], key=lambda x: (-x[1], x[0]))
#     print(scores)
#     result = [0] * 11
#     for score in scores:
#         arrows = info[10 - score[0]] + 1
#         if sum(result) + arrows > n:
#             continue
#         result[10 - score[0]] = arrows
#         info[10 - score[0]] = 0
#         if n == sum(result):
#             break
#     else:
#         result[-1] = n - sum(result)

#     apeach = sum([10 - i for i, s in enumerate(info) if s > 0])
#     ryan = sum([10 - i for i, s in enumerate(result) if s > 0])
#     print(f'Ryan: {ryan}, Apeach: {apeach}, Diff: {ryan - apeach}')
#     return result if ryan > apeach else [-1]