from heapq import *

def solution(jobs):
    jobs_count = len(jobs)
    jobs = [(x[0], x[1], i) for i, x in enumerate(jobs)]
    jobs.sort(key = lambda x : (-x[0], -x[1]))
    que = []
    
    cur = 0
    answer = 0
    while que or jobs :
        # to que from jobs
        while jobs and jobs[-1][0] <= cur :
            x1, x2, x3 = jobs.pop()
            heappush(que, (x2, x1, x3))
        
        # work
        if que :
            x1, x2, x3 = heappop(que)
            cur += x1
            answer += cur - x2
        else :
            cur = jobs[-1][0]
            
    return answer // jobs_count