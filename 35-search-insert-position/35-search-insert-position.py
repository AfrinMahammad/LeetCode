class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if nums[0]>=target:
            return 0
        elif nums[n-1]==target:
            return n-1
        elif nums[n-1]<target:
            return n
        low,high,mid=0,n-1,0
        while low<high:
            temp=mid
            mid=(high+low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1 
        if temp>mid:
            for i in range(mid,temp+2):
                if nums[i]>=target:
                    return i
        else:
            for i in range(temp,mid+2):
                if nums[i]>=target:
                    return i
            