class Solution:
    def minCost(self, colors: str, t: List[int]) -> int:
        n=len(colors)
        res=0
        t1,t2=0,1
        while t2<n:
            print(t1,t2,res)
            if colors[t1]==colors[t2]:
                if t[t1]<t[t2]:
                    res+=t[t1]
                    t2+=1
                    t1=t2-1
                else:
                    res+=t[t2]
                    t2+=1
            else:
                t2+=1
                t1=t2-1
        return res