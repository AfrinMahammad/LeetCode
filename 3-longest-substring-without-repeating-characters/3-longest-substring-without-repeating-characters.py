class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        for i in range(0,len(s)):
            t=s[i]
            for j in range(i+1,len(s)):
                if s[j] in t:
                    break
                else:
                    t=t+s[j]
            if res<len(t):
                res=len(t)
        return res