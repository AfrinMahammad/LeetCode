class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in range(0,len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                l.append(s[i])
            elif s[i]==')' or s[i]=='}' or s[i]==']':
                if len(l)==0:
                    return False
                else:
                    t=l.pop()
                    if t=='(' and s[i]!=')':
                        return False
                    elif t=='[' and s[i]!=']':
                        return False
                    elif t=='{' and s[i]!='}':
                        return False
        if len(l)!=0:
            return False
        return True