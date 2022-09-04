class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        x=-1
        for i in range(0,n):
            if nums[i]>0:
                x=i
                break
        if x==-1 or nums[i]>1:
            return 1
        else:
            x=nums[i]
            for i in range(i,n):
                if nums[i]!=x and nums[i]!=x+1:
                    return x+1
                else:
                    x=nums[i]
        return nums[-1]+1