class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        d={}
        res=[]
        n=len(nums)
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]>(n//3):
                res.append(i)
        return res