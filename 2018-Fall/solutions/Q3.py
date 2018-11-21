def isIsomorphic(s,t):
        mapx = {}
        for i in range(len(s)):
            if s[i] not in mapx:
                mapx[s[i]] = t[i]
            elif s[i] in mapx:
                if t[i] != mapx[s[i]]:
                    return False
        return True

A = 'paper'
B = 'later'

print isIsomorphic(A, B)
