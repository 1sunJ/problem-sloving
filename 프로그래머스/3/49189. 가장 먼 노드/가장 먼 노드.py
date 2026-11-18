import heapq

def solution(n, edge):
    
    graph = [[] for _ in range(n + 1)]
    for a, b in edge :
        graph[a].append(b)
        graph[b].append(a)
    
    dist = [10 ** 5] * (n + 1)
    dist[1] = 0
    hq = [(0, 1)]
    
    while hq :
        d, p = heapq.heappop(hq)
        if dist[p] < d :
            continue
            
        for next in graph[p] :
            if d + 1 < dist[next] :
                dist[next] = d + 1
                heapq.heappush(hq, (d + 1, next))
    
    for i, x in enumerate(dist) :
        dist[i] = x if x != 10 ** 5 else -1
    
    return dist.count(max(dist))