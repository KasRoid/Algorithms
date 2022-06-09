# 주차 요금 계산
# https://programmers.co.kr/learn/courses/30/lessons/92341

from datetime import datetime
import math

def solution(fees, records):
    base_seconds = fees[0] * 60
    base_rate = fees[1]
    additional_seconds = fees[2] * 60
    additional_rate = fees[3]
    records = [record.split() for record in records]
    cache = {}

    for record in records:
        time = record[0]
        car_number = record[1]
        if car_number in cache:
            cache[car_number].append(time)
        else:
            cache[car_number] = [time]

    for key, value in cache.items():
        if len(value) % 2:
            value.append('23:59')
        temp = []
        for i in range(len(value) // 2):
            start_time = datetime.strptime(value[i * 2], '%H:%M')
            end_time = datetime.strptime(value[i * 2 + 1], '%H:%M')
            diff = (end_time - start_time).total_seconds()
            temp.append(diff)
        cache[key] = sum(temp)
    
    for key, value in cache.items():
        additional_charge = math.ceil((value - base_seconds) / additional_seconds) * additional_rate
        cache[key] = base_rate if value <= base_seconds else base_rate + additional_charge
    return [fee[1] for fee in sorted(cache.items(), key=lambda x: x[0])]


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", 
"07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", 
"19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))  # [14600, 34400, 5000]
