class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        c=0
        while i<len(nums)-c:
            if nums[i]==0:
                del nums[i]
                nums.append(0)
                c+=1
                i-=1
            i+=1
        return nums