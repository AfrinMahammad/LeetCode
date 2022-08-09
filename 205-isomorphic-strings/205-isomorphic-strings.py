class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1,d2={},{}
        for i in range(0,len(s)):
            if (s[i] not in d1) and (t[i] not in d2):
                d1[s[i]]=t[i]
                d2[t[i]]=s[i]
            elif (s[i] in d1 and d1[s[i]]!=t[i]) or (t[i] in d2 and d2[t[i]]!=s[i]):
                return False
        return True