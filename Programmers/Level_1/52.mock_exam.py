# 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840


def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = {p: 0 for p in range(1, 4)}

    for i, answer in enumerate(answers):
        if p1[i % len(p1)] == answer:
            scores[1] += 1
        if p2[i % len(p2)] == answer:
            scores[2] += 1
        if p3[i % len(p3)] == answer:
            scores[3] += 1
    max_value = max(scores.values())
    max_scores = filter(lambda x: x[1] == max_value, scores.items())
    sorted_scores = sorted(max_scores, key=lambda x: x[1], reverse=True)
    return list(map(lambda x: x[0], sorted_scores))


print(solution([1, 2, 3, 4, 5]))  # [1]
print(solution([1, 3, 2, 4, 2]))  # [1,2,3]
