class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=list()
        for i in range(n//2):
            l+=[nums[(2*i)+1]]*nums[2*i]
        return l


        
