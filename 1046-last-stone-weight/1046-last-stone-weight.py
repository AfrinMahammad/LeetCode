class Solution:
    def lastStoneWeight(self, s: List[int]) -> int:
        if len(s)==1:
            return s[0]
        s.sort(reverse=True)
        while len(s)>1:
            if s[0]==s[1]:
                s.pop(1)
                s.pop(0)
            else:
                s[0]=s[0]-s[1]
                s.pop(1)
            s.sort(reverse=True)
        if len(s)==0:
            return 0
        return s[0]