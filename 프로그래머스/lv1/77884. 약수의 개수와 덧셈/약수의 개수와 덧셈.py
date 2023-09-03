def solution(left, right):
    answer = 0
    count = 0
    if left == right:
        for i in range(1,left+1):
            if left % i == 0:
                count += 1
        if count % 2 == 0:
            answer = left
        else:
            answer = 0
    else:
        for i in range(left,right+1):
            count = 0
            for j in range(1,i+1):
                if i % j == 0:
                    count += 1
            if count % 2 == 0:
                answer += i
            else:
                answer -= i
    return answer