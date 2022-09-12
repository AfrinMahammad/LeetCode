class Solution:
    def checkValid(self, m: List[List[int]]) -> bool:
        n=len(m)
        s=[i for i in range(1,n+1)]
        for i in range(0,n):
            if sorted(m[i])!=s:
                return False
        for i in range(0,n):
            l=[]
            for j in range(0,n):
                l.append(m[j][i])
            if sorted(l)!=s:
                return False
        return True