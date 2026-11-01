def solution(n):
    
    sqrt = n ** 0.5
    
    if sqrt - int(sqrt) == 0 :
        return (sqrt + 1) ** 2
    else :
        return -1