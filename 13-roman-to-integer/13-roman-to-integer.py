class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        temp=0
        mapping={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in s[::-1]:
            if mapping[i]>=temp:
                res+=mapping[i]
            else:
                res-=mapping[i]
            temp=mapping[i]
        return res