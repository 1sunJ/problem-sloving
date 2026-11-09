from heapq import *

def solution(operations):
    mp = dict()
    max_h = []
    min_h = []
    
    for o in operations :
        c, v = o.split()
        v = int(v)
        if c == 'I' :
            if v in mp :
                mp[v] += 1
            else :
                mp[v] = 1
            heappush(max_h, -v)
            heappush(min_h, v)
        else :
            if not sum(mp.values()) :
                continue
            h = max_h if v == 1 else min_h
            while True :
                x = heappop(h)
                if v == 1 :
                    x = -x
                if x in mp :
                    mp[x] -= 1
                    if mp[x] == 0 :
                        del mp[x]
                    break
    
    answer = [0, 0]
    while max_h :
        x = -heappop(max_h)
        if x in mp :
            answer[0] = x
            break
    while min_h :
        x = heappop(min_h)
        if x in mp :
            answer[1] = x
            break
            
    return answer
            
            