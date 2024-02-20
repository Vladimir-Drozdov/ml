def naive(t, p):
    n = len(t)
    m = len(p)
    ans = []
    for s in range(n-m+1):
        if t[s:(s+m)] == p:
            ans.append(s)
    if(ans==[]):
        return -1
    return ans
