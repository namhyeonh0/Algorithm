def solution(a, b):
    answer = ''
    date = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8 : 31, 9: 30, 10: 31, 11: 30, 12: 31}
    days = 0
    for i in range(1,a):
        days += month[i]
    days += b
    plus = (days - 1) % 7 
    answer = date[plus]
    return answer