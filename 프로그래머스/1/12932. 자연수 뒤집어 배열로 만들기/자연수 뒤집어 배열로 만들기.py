def solution(n):
    s = str(n) # '12345'
    arr = list(s) # ['1', '2', '3', '4', '5']
    arr = list(map(int, arr)) # map(func, iterable)
    arr = arr[::-1]
    return arr