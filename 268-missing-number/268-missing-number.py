class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        l=[i for i in range(0,n+1)]
        return list(set(l)-set(nums))[0]