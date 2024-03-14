def solution(n, t, m, p):
    answer = ''
    
    nums = ""
    a = 0
    while len(nums) <= t*m:
        nums += nnn(a,n)
        a += 1
        
    for i in range(t):
        answer += nums[(p-1)+m*i]
        
    return answer

def nnn(a,n):
    answer = ""
    r10 = {10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F"}
    
    if a == 0:
        answer += "0"
    else:
    
        while a:
            q,r = divmod(a,n)
            if r >= 10:
                answer += r10[r]
            else:
                answer += str(r)
            a = q
    
    return answer[::-1]
        