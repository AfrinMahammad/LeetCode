class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        for i in range(0,len(nums)):
            lsum=sum(nums[0:i])
            if lsum==s-nums[i]-lsum:
                return i
        return -1