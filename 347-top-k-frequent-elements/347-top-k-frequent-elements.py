class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for  i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d=sorted(d,key=lambda x:(-d[x],x))[:k]
        return d