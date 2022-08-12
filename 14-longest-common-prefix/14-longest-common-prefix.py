class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        n,j=200,0
        for i in strs:
            x=len(i)
            if n>len(i):
                n=len(i)
        while j<n:
            s=strs[0][:j+1]
            flag=1
            for i in range(0,len(strs)):
                if strs[i].startswith(s)==0:
                    flag=0
                    break
            if flag==0:
                res=strs[0][:j]
                return res
            else:
                res=s
            j+=1
        return res