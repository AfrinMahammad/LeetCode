class Solution:
    def plusOne(self, num: List[int]) -> List[int]:
        s=""
        for i in num:
            s=s+str(i)
        n=int(s)
        res=[]
        for i in str(n+1):
            res.append(int(i))
        return res