class Solution:
    def reverseWords(self, s: str) -> str:
        x=s.split(" ")
        res=""
        for i in x[::-1]:
            if i!='':
                res+=i+" "
        return res.strip()       
                
                
        