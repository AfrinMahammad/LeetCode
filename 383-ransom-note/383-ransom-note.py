class Solution:    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        for i in magazine:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in ransomNote:
            if i not in d:
                return False
            elif d[i]>0:
                d[i]-=1
            else:
                return False
        return True
            