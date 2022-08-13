class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res=[]
        l=len(words)*len(words[0])
        wl=len(words[0])
        for i in range(0,len(s)-l+1):
            t=[]
            sub=s[i:i+l]
            for j in range(0,len(sub),wl):
                t.append(sub[j:j+wl])
            if sorted(t)==sorted(words):
                res.append(i)
        return res