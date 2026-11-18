import heapq

INF = float('inf')

def solution(N, road, K):
    answer = 0
    
    graph = [[] for _ in range(N + 1)]
    for a, b, w in road :
        graph[a].append((b, w))
        graph[b].append((a, w))
    
    dist = [INF] * (N + 1)
    dist[1] = 0
    hq = [(0, 1)]
    
    while hq :
        d, p = heapq.heappop(hq)
        
        if dist[p] < d :
            continue
            
        for next, w in graph[p] :
            if dist[next] > d + w :
                dist[next] = d + w
                heapq.heappush(hq, (dist[next], next))
    
    return [x <= K for x in dist].count(True)