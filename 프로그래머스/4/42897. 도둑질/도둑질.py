def solution(mny):
    # mny = [1, 3, 2 ,4, 5, 6, 8, 9]
    
    dp1 = [0] * len(mny)
    dp2 = [0] * len(mny)
    dp1[0] = mny[0]
    dp2[-1] = mny[-1]
    
    for i in range(len(mny) - 2) :
        dp1[i+1] = dp1[i-1] + mny[i+1]
        dp1[i+1] = max(dp1[i+1], dp1[i-2] + mny[i+1])
        
        dp2[i] = dp2[i-2] + mny[i]
        dp2[i] = max(dp2[i], dp2[i-3] + mny[i])
        
    # print(dp1)
    # print(dp2)
    
    return max(max(dp1), max(dp2))