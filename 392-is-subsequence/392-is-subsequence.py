class Solution:
    def findindex(self, t:str,x:str,k:int)->int:
        for i in range(k,len(t)):
            if t[i]==x:
                return i
        return -1
    def isSubsequence(self, s: str, t: str) -> bool:
        k=-1
        for i in s:
            if i not in t:
                return False
            n=Solution().findindex(t,i,k+1)
            if n==-1:
                return False
            elif k>n:
                return False
            else:
                k=n
        return True