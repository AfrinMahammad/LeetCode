class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        n=len(s)
        i=0
        while i<n:
            if s[i].isalnum()==0 or s[i]==" ":
                n-=1
                if i==len(s)-1:
                    s=s[:i]
                else:
                    s=s[:i]+s[i+1:]
            else:
                i+=1
        if s==s[::-1]:
            return True
        else:
            return False