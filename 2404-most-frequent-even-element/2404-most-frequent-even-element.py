class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i%2==0:
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
        if d=={}:
            return -1
        d=sorted(d,key=lambda x:(-d[x],x))
        return d[0]