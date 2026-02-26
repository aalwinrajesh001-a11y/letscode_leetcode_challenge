class Solution:
    def averageValue(self, nums: List[int]) -> int:
        cnt,sm=0,0
        n=len(nums)
        for i in range (n):
            if nums[i]%6==0:
                sm+=nums[i]
                cnt+=1
        if cnt!=0:
            return int(sm/cnt)
        else:
            return 0
          
