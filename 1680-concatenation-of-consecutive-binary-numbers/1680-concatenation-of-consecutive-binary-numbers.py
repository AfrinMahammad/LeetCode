class Solution:
    def concatenatedBinary(self, n: int) -> int:
        m=pow(10,9)+7
        res=""
        for i in range(1,n+1):
            res+=str(format(i,'b'))
        return int(res,2)%m