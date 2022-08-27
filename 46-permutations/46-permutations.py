class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        p=[]
        for i in range(0,len(nums)):
            x=Solution().permute(nums[:i]+nums[i+1:])
            for k in x:
                k.insert(0,nums[i])
                p.append(k)
        return p