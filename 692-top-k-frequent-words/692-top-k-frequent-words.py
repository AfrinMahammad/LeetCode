from collections import OrderedDict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d={}
        for i in words:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        res=sorted(d,key=lambda x:(-d[x],x))
        return res[:k]