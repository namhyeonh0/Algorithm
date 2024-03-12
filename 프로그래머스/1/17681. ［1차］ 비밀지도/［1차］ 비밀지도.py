def solution(n, arr1, arr2):
    answer = []
    s = '0' + str(n) + 'b'
    for i in range(n):
        a = format(arr1[i],s)
        b = format(arr2[i],s)
        c = ''
        for j in range(n):
            if a[j] == '1' or b[j] == '1':
                c += '#'
            else:
                c += ' '
        answer.append(c)
        
    return answer