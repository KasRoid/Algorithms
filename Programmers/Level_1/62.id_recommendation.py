# 신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3

import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub("[^A-Za-z0-9-_.]+", "", new_id)
    new_id = re.sub("[.]{2,}", ".", new_id)
    if new_id[0:1] == ".":
        new_id = new_id[1:]
    if new_id[-1:] == ".":
        new_id = new_id[0:-1]
    if new_id == "":
        new_id = "a"
    if len(new_id) > 15:
        new_id = new_id[:15]
    if new_id[-1:] == ".":
        new_id = new_id[0:-1]
    while len(new_id) < 3:
        new_id += new_id[-1:]
    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))  # "bat.y.abcdefghi"
print(solution("123_.def"))  # "123_.def"
