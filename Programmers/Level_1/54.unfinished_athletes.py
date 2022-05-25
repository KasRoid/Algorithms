# 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576


def solution(participant, completion):
    participant_set = set(participant)
    if len(participant) == len(participant_set):
        return (participant_set - set(completion)).pop()
    else:
        dup_dic = {}
        comp_dic = {p: 0 for p in completion}
        temp = set()
        completion.append(None)
        for p, c in zip(participant, completion):
            if p in temp:
                dup_dic[p] = dup_dic[p] + 1 if p in dup_dic else 2
            else:
                temp.add(p)
            if c in comp_dic:
                comp_dic[c] += 1
        for d in dup_dic.keys():
            if dup_dic[d] > comp_dic[d]:
                return d
        return (participant_set - set(completion)).pop()
            

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))  # "leo"
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))  # "vinko"
print(solution(["mislav", "mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav", "mislav"]))  # "mislav"
