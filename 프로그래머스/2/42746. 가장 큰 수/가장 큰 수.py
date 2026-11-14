def solution(arr) :
    arr = list(map(str, arr))
    arr.sort(key = lambda x : x * 3, reverse=True)
    
    if arr[0][0] == '0' :
        return '0'
    
    return ''.join(arr)