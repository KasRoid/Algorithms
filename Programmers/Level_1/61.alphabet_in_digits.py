# 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3

def solution(s):
    answer = ''
    num_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    i = 0
    j = 0
    while j < len(s):
        word = s[i:j + 1]
        if word.isdigit():
            i += 1
            answer += word
        if word in num_dict:
            i += len(word)
            answer += num_dict[word]
        j += 1
    return int(answer)


print(solution("one4seveneight"))  # 1478
