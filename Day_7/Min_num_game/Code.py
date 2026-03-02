class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=list()
        nums.sort()
        for i in range(len(nums)//2):
            arr.append(nums[2*i+1])
            arr.append(nums[2*i])
        return arr
      
