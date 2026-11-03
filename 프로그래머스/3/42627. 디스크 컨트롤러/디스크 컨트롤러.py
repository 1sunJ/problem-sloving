from heapq import *

def solution(jobs):
    # 자료구조 변경 -> [(소요 시간, 요청 시각, 작업 번호), ...]
    arr = []
    for i, x in enumerate(jobs) :
        arr.append((x[1], x[0], i))
    
    heapify(arr)
    print(arr)
    answer = 0
    return answer