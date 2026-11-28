def solution(num_str):
    n = int(num_str)
    
    answer = 0
    while n :
        answer += n % 10
        n //= 10
        
    return answer