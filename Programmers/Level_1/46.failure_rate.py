# 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    total_users = len(stages)
    stages = sorted(stages)
    record = {level: 0 for level in range(1, N + 1)}
    result = [*range(1, N + 1)]

    for level in range(1, N + 1):
        failure_count = 0
        while level == stages[failure_count]:
            failure_count += 1
            if failure_count == len(stages):
                break
        record[level] = failure_count / total_users
        total_users -= failure_count
        stages = stages[failure_count:]

        if record[level]:
            index = result.index(level)
            current_stage = result.pop(index)
            for i, value in enumerate(result):
                if record[level] > record[value]:
                    result.insert(i, current_stage)
                    current_stage = None
                    break
            if current_stage:
                result.append(current_stage)
        if len(stages) == 0:
            break
    return result


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))  # [3,4,2,1,5]
print(solution(4, [4,4,4,4,4]))  # [4,1,2,3]
