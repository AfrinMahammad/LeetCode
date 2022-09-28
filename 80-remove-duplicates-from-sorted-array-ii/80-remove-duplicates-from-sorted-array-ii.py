class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        while i<len(nums):
            if nums[i-1]==nums[i] :
                j=i+1
                while j<len(nums) and nums[i]==nums[j]:
                    del nums[j]
                    print(i,j,nums)
                i+=2
            else:
                i+=1
        return len(nums)
                    