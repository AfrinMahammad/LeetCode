class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n=len(arr)
        if n==2:
            return 1
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        if len(d)==1:
            return 1
        x=sorted(list(d.values()),reverse=True)
        s=0
        for i in range(0,len(x)):
            s+=x[i]
            if s>=n/2:
                return i+1