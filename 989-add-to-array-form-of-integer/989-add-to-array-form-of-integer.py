class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=""
        for i in num:
            s=s+str(i)
        n=int(s)
        res=[]
        for i in str(n+k):
            res.append(int(i))
        return res