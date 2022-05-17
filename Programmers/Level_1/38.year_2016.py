# 2016년
# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    weekday = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    cal = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    days = 0
    for i in range(1, a):
        days += cal[i]
    return weekday[(4 + b + days) % 7]
    

print(solution(5, 24))
