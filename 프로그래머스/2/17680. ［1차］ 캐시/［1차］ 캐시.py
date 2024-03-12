from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque([])
    
    for i in cities:
        a = i.lower()
        if cacheSize == 0:
            answer += 5
            continue
        elif len(cache) < cacheSize and a not in cache:
            cache.append(a)
            answer += 5
            continue
        elif len(cache) < cacheSize and a in cache:
            answer += 1
            cache.remove(a)
            cache.append(a)
            continue
        else:
            if a in cache:
                answer += 1
                cache.remove(a)
                cache.append(a)
            else:
                answer += 5
                cache.popleft()
                cache.append(a)
            
    return answer