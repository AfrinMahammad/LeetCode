class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        t=sorted(d,key=lambda x:(-d[x],x))
        res=""
        for i in t:
            res+=i*d[i]
        return res