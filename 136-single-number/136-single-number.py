class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x=nums.pop(i)
            if x not in nums:
                return x
            else:
                nums.insert(i,x)