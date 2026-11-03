from heapq import *

def solution(arr, K):
    
    heapify(arr)
    
    cnt = 0 
    while len(arr) > 1 and arr[0] < K :
        n1 = heappop(arr)
        n2 = heappop(arr)
        new = n1 + n2 * 2
        heappush(arr, new)
        cnt += 1
        
    return cnt if arr[0] >= K else -1
    
    
    