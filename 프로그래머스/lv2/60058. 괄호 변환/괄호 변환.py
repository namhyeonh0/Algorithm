def solution(p):
    
    goodString = ''
    
    def decompose(a):
        left, right = 0, 0
        u, v = '', ''
        for i in range(len(a)):
            if a[i] == '(':
                left += 1
                u += a[i]
            elif a[i] == ')':
                right += 1
                u += a[i]
            if left == right:
                v = a[i+1:]
                break
        return u, v
                
    def is_good(b):
        if b[0] == ')':
            good = False
        else:
            good = True
        return good
    
    def u_toGood(a):
        good = ''
        if len(a) == 2:
            good = ''
        else:
            a = a[1:len(a)-1]
            for i in a:
                if i == '(':
                    good += ')'
                else:
                    good += '('
        return good
    
    def toGood(a,b):
        if is_good(a) == True and len(b) != 0:
            c, d = decompose(b)
            print('True and not zero')
            return a + toGood(c,d)
        elif is_good(a) == True and len(b) == 0:
            print('True and zero')
            return a
        elif is_good(a) == False and len(b) != 0:
            new_u, new_v = decompose(b)
            new_a = u_toGood(a)
            print('False and not zero')
            return '(' + toGood(new_u,new_v) + ')' + new_a
        elif is_good(a) == False and len(b) == 0:
            new_a = u_toGood(a)
            print('False and zero')
            return '(' + ')' + new_a
        
        
            
            
            
    
    u,v = decompose(p)
    k = toGood(u,v)
            
    return k