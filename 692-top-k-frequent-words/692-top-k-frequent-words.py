from collections import OrderedDict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res=[]
        d={}
        for i in words:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        values=sorted(list(d.values()),reverse=True)
        d=OrderedDict(sorted(d.items()))
        for i in range(0,k):
            res.append(list(d.keys())[list(d.values()).index(values[i])])
            d.pop(res[-1])
        return res    
        