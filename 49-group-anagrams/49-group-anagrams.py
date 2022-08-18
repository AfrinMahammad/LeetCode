class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        n=len(strs)
        if n==1:
            return [strs]
        res={}
        for i in range(0,n):
            s="".join(sorted(strs[i]))
            if s in res:
                res[s].append(strs[i])
            else:
                res[s]=[strs[i]]   
        return list(res.values())