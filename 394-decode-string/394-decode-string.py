class Solution:
    def decodeString(self, s: str) -> str:
        res=""
        b1,b2=0,0
        i=len(s)-1
        while i>=0:
            if s[i].isnumeric():
                b2=i
                while s[i].isnumeric():
                    i-=1
                b1=i+1
                n=int(s[b1:b2+1])
                j=b2+1
                while s[j]!=']':
                    j+=1
                s=s[:b1]+n*s[b2+2:j]+s[j+1:]
            else:
                i-=1
        return s