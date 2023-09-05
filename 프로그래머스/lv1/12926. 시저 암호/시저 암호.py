def solution(s, n):
    answer = ''
    a_low = ord('a')
    z_low = ord('z')
    a_upp = ord('A')
    z_upp = ord('Z')
    for i in s:
        if i == ' ':
            answer += i
        else:
            if i.isupper() == True:
                if (ord(i) + n) > z_upp:
                    answer += chr(a_upp+ord(i)+n-z_upp-1)
                else:
                    answer += chr(ord(i)+n)
            else:
                if (ord(i) + n) > z_low:
                    answer += chr(a_low+ord(i)+n-z_low-1)
                else:
                    answer += chr(ord(i)+n)
    return answer