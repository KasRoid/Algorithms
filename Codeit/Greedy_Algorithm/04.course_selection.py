# 리스트에 들어있는 튜플은 각 수업의 시작시간과 끝시간이다.
# 수업시간이 겹치지 않고 가장 많이 들을 수 있는 경우를 출력하는 함수 구현

def course_selection(course_list):
    result = []
    for course in sorted(course_list, key=lambda item: item[1]):
        if len(result) == 0:
            result.append(course)
        else:
            end_time = result[-1][1]
            start_time = course[0]
            if start_time >= end_time:
                result.append(course)
    return result


# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
