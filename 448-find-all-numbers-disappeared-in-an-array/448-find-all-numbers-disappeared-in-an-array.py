class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=[i for i in range(1,len(nums)+1)]   
        return list(set(l)-set(nums))