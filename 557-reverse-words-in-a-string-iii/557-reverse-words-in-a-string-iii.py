class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split(' ')
        res=""
        n=len(l)
        for i in range(n):
            res+=l[i][::-1]
            if i!=n-1:
                res+=" "
        return res