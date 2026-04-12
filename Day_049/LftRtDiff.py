class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        lsum=[0]*n
        rsum=[0]*n
        ans=[0]*n
        l=0
        r=sum(nums)

        for i in range(n-1):
            l+=nums[i]
            r-=nums[i]
            lsum[i+1]=l
            rsum[i]=r
            ans[i]=abs(lsum[i]-rsum[i])
        ans[n-1]=abs(lsum[n-1]-rsum[n-1])
        return ans
        


