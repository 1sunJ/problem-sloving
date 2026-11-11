def solution(s):
    st = []
    
    for c in s :
        if not st :
            st.append(c)
            continue
            
        if st[-1] == c :
            st.pop()
        else :
            st.append(c)
            
    return int(not bool(st))