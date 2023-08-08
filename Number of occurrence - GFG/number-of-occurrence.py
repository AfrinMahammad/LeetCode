#User function Template for python3
class Solution:
    def helper(self,arr,index,x):
        i,j=index,index+1
        c=0
        while i>=0 and arr[i]==x:
            c+=1
            i-=1
        while j<n and arr[j]==x:
            c+=1
            j+=1
        return c
	def count(self,arr, n, x):
		# code here
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==x:
                return self.helper(arr,mid,x)
            elif arr[mid]>x:
                r=mid-1
            else:
                l=mid+1
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends