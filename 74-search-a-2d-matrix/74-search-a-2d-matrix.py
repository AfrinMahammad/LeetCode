class Solution:
    def searchMatrix(self, m: List[List[int]], target: int) -> bool:
        for i in range(len(m)):
            if m[i][-1]==target:
                return True
            elif m[i][-1]>target:
                l,r=0,len(m[i])-1
                while l<=r:
                    mid=(l+r)//2
                    if m[i][mid]==target:
                        return True
                    elif m[i][mid]>target:
                        r=mid-1
                    elif m[i][mid]<target:
                        l=mid+1
        return False