class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        left=0
        right=sum(nums[1:])
        for i in range(0,n):
            if left==right:
                return i
            if i==n-1:
                break
            left+=nums[i]
            right-=nums[i+1]
        return -1