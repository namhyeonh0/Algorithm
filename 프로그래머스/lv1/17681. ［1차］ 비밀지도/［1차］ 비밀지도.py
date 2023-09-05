def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        a = format(arr1[i],'b')
        b = format(arr2[i],'b')
        c = ''
        if len(a) < len(arr1):
            a = '0' * (len(arr1)-len(a)) + a
        if len(b) < len(arr1):
            b = '0' * (len(arr1)-len(b)) + b
        for j in range(len(a)):
            if a[j] == b[j] and a[j] == '0':
                c += ' '
            elif a[j] == b[j] and a[j] == '1':
                c += '#'
            elif a[j] != b[j]:
                c += '#'
        answer.append(c)
    return answer