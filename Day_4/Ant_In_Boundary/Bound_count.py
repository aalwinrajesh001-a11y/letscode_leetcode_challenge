class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        pos=0
        count=0
        for i in nums:
            pos+=i
            if pos==0:
                count+=1
        return count
      
