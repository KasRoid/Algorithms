# 신고 결과 받기
# https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    report_dic = {user: set() for user in id_list}
    result = [0] * len(id_list)

    for r in report:
        reporter, reported_user = r.split()
        report_dic[reported_user].add(reporter)
    user_list = sum([list(users) for users in report_dic.values() if len(users) >= k], [])
    
    for user in user_list:
        result[id_list.index(user)] += 1
    return result


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
